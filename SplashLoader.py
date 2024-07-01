import maya.cmds as cmds
import os
import shutil

# Function to copy and backup the custom splash image to the approriate paths.
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
    cmds.confirmDialog(title="Success", message="Splash screen updated. Please restart Maya to see the changes.", button=["OK"])

# Function to open a file dialog to select a custom splash image
def select_image_and_set_splash_screen(text_field, *args):
    # Open a file dialog to select an image
    image_path = cmds.fileDialog2(fileFilter="*.png", dialogStyle=2, fm=1)
    if image_path:
        set_splash_screen(image_path[0], text_field)

# Check if the window exists and delete it if it does
if cmds.window("setSplashScreenWin", exists=True):
    cmds.deleteUI("setSplashScreenWin", window=True)

# Create a new window
window = cmds.window("setSplashScreenWin", title="Maya Splash Changer", sizeable=False)
cmds.columnLayout(adjustableColumn=True, columnAttach=['both', 10], rowSpacing=10)
cmds.separator(height=10)
cmds.text(label="Please use the button below to select your splash screen image:")
text_field = cmds.textFieldButtonGrp(bl="Select Image", bc=lambda *args: select_image_and_set_splash_screen(text_field, *args), ed=False, adjustableColumn=True, en=True)
cmds.button(label="Close", command=('cmds.deleteUI(\"' + window + '\", window=True)'))
cmds.separator(height=10)
cmds.setParent('..')
cmds.showWindow(window)
