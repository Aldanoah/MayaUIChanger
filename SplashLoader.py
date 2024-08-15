import maya.cmds as cmds
import os
import shutil
import winsound
import json

# Define the path for the settings file
settings_file_path = os.path.expanduser("~/.maya_splash_settings.json")

# Function to save settings to a JSON file
def save_settings(audio_file_path):
    settings = {"audio_file": audio_file_path}
    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

# Function to load settings from a JSON file
def load_settings():
    if os.path.isfile(settings_file_path):
        with open(settings_file_path, 'r') as f:
            return json.load(f)
    return {}

# Function to copy and backup the custom splash image to the appropriate paths.
def set_splash_screen(image_path, text_field):
    # Verify the image path exists
    if not os.path.isfile(image_path):
        cmds.error("Selected file does not exist.")
        return
    
    # Update the window text field with the selected file name
    cmds.textFieldButtonGrp(text_field, e=True, text=os.path.basename(image_path))
    
    # Define the target path for the splash screen, Adjust Maya version as needed.
    maya_install_path = r"C:\Program Files\Autodesk\Maya2024"  
    splash_screen_dir = os.path.join(maya_install_path, "icons")
    splash_screen_path = os.path.join(splash_screen_dir, "MayaStartupImage.png")
    
    # Backup the original splash screen if it hasn't been backed up yet
    original_splash_screen_backup = os.path.join(splash_screen_dir, "MayaStartupImage_backup.png")
    if not os.path.isfile(original_splash_screen_backup) and os.path.isfile(splash_screen_path):
        shutil.copyfile(splash_screen_path, original_splash_screen_backup)
    
    # Copy the selected image to the new splash screen path
    shutil.copyfile(image_path, splash_screen_path)
    cmds.confirmDialog(title="Success", message="Splash set successfully. Please restart Maya to effect changes.", button=["OK"])

# Function to open a file dialog to select a custom splash image
def select_image_and_set_splash_screen(text_field, *args):
    # Open a file dialog to select an image
    image_path = cmds.fileDialog2(fileFilter="*.png", dialogStyle=2, fm=1)
    if image_path:
        set_splash_screen(image_path[0], text_field)

# Function to open a file dialog to select a custom audio file
def select_audio(text_field, *args):
    # Open a file dialog to select an audio file
    audio_path = cmds.fileDialog2(fileFilter="*.wav", dialogStyle=2, fm=1)
    if audio_path:
        cmds.textFieldButtonGrp(text_field, e=True, text=os.path.basename(audio_path[0]))
        save_settings(audio_path[0])
        cmds.confirmDialog(title="Success", message="File set successfully. Please restart Maya to effect changes.", button=["OK"])

# Function to play the selected custom sound
def play_custom_sound(sound_file):
    try:
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Callback to show/hide audio file selection based on the checkbox state
def toggle_audio_file_field(checkbox, text_field):
    is_checked = cmds.checkBox(checkbox, q=True, value=True)
    cmds.textFieldButtonGrp(text_field, e=True, visible=is_checked)

# Load settings and play the saved custom sound if available
settings = load_settings()
if 'audio_file' in settings:
    play_custom_sound(settings['audio_file'])

# This function encapsulates the UI code and is only called when needed
def show_splash_tool_window():
    if cmds.window("setSplashScreenWin", exists=True):
        cmds.deleteUI("setSplashScreenWin", window=True)
    window = cmds.window("setSplashScreenWin", title="Splash Tool", sizeable=False)
    cmds.columnLayout(adjustableColumn=True, columnAttach=['both', 10], rowSpacing=10)
    cmds.separator(height=10)
    audio_checkbox = cmds.checkBox(label="Enable Startup Sound?", changeCommand=lambda *args: toggle_audio_file_field(audio_checkbox, audio_text_field))
    cmds.text(label="Please use the button below to select your desired file:")
    image_text_field = cmds.textFieldButtonGrp(bl="Select Image File", bc=lambda *args: select_image_and_set_splash_screen(image_text_field, *args), adjustableColumn=True)
    audio_text_field = cmds.textFieldButtonGrp(bl="Select Audio File", bc=lambda *args: select_audio(audio_text_field, *args), adjustableColumn=True, visible=False)
    cmds.button(label="Close", command=('cmds.deleteUI(\"' + window + '\", window=True)'))
    cmds.separator(height=10)
    cmds.setParent('..')
    cmds.showWindow(window)

# Ensuring that the window only opens when this script is run directly
if __name__ == "__main__":
    show_splash_tool_window()