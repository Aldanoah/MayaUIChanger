import os
import sys
import shutil
import winsound
import json
import glob
import maya.utils
try:
    from PySide6 import QtWidgets, QtCore
    import shiboken6 as shiboken
except ImportError:
    from PySide2 import QtWidgets, QtCore
    import shiboken2 as shiboken
    
import maya.OpenMayaUI as omui

# ---------------- Settings ----------------
settings_file_path = os.path.expanduser("~/.maya_splash_settings.json")

def save_settings(audio_file_path=None):
    if audio_file_path:
        settings = {"audio_file": audio_file_path}
    else:
        settings = {}
    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

def load_settings():
    if os.path.isfile(settings_file_path):
        with open(settings_file_path, 'r') as f:
            return json.load(f)
    return {}

# ---------------- Maya Install Path Detection ----------------
def get_maya_install_path():
    if "maya" in os.path.basename(sys.executable).lower():
        return os.path.dirname(os.path.dirname(sys.executable))
    maya_env = os.environ.get("MAYA_LOCATION")
    if maya_env and os.path.exists(maya_env):
        return maya_env
    maya_root = r"C:\Program Files\Autodesk"
    maya_dirs = glob.glob(os.path.join(maya_root, "Maya*"))
    if maya_dirs:
        return sorted(maya_dirs)[-1]
    raise RuntimeError("Unable to locate Maya installation.")

def find_splash_image_path(maya_install_path):
    splash_dir = os.path.join(maya_install_path, "icons")
    possible_names = [
        "MayaStartupImage.png",
        "MayaStartupHD.png",
        "MayaStartupImageHD.png",
        "StartupImage.png",
        "splash.png",
    ]
    for name in possible_names:
        path = os.path.join(splash_dir, name)
        if os.path.isfile(path):
            return path
    return os.path.join(splash_dir, possible_names[0])

# ---------------- Splash Handling ----------------
def set_splash_screen(image_path, text_field=None):
    if not os.path.isfile(image_path):
        QtWidgets.QMessageBox.warning(None, "Error", "Selected file does not exist.")
        return
    if text_field:
        text_field.setText(os.path.basename(image_path))
    maya_install_path = get_maya_install_path()
    splash_screen_path = find_splash_image_path(maya_install_path)
    splash_screen_dir = os.path.dirname(splash_screen_path)
    backup_path = os.path.join(splash_screen_dir, os.path.basename(splash_screen_path).replace(".png", "_backup.png"))
    if not os.path.isfile(backup_path) and os.path.isfile(splash_screen_path):
        shutil.copyfile(splash_screen_path, backup_path)
    shutil.copyfile(image_path, splash_screen_path)
    QtWidgets.QMessageBox.information(None, "Success", "Splash set successfully. Please restart Maya to see the changes.")

# ---------------- Audio Handling ----------------
startup_sound_played = False

def load_audio_file():
    """Load the audio file path safely from settings."""
    settings = load_settings()
    audio_file = settings.get("audio_file")
    # Ensure we only return a string path
    if isinstance(audio_file, str) and os.path.isfile(audio_file):
        return audio_file
    return None

def save_audio_file(audio_file_path=None):
    """Save audio file path to settings safely."""
    settings = {}
    if isinstance(audio_file_path, str):
        settings["audio_file"] = audio_file_path
    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

audio_file = load_audio_file()

if audio_file:
    def play_startup_sound_once():
        global startup_sound_played
        if not startup_sound_played:
            startup_sound_played = True
            try:
                winsound.PlaySound(audio_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"Error playing startup sound: {e}")

    # Deferred to run after Maya loads
    maya.utils.executeDeferred(play_startup_sound_once)
    
# ---------------- Build Splash UI ----------------
def maya_main_window():
    ptr = omui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(int(ptr), QtWidgets.QWidget)

class SplashToolWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SplashToolWindow, self).__init__(parent)
        self.setWindowTitle("Splash Tool")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(350)
        self.setModal(False)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui_initialized = False
        self.settings = load_settings()

        self.build_ui()
        self.ui_initialized = True

    def build_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setSpacing(10)

        # --- Enable/Disable Audio ---
        layout.addWidget(QtWidgets.QLabel("Do you want to enable sound on startup?"), alignment=QtCore.Qt.AlignCenter)
        self.enable_radio = QtWidgets.QRadioButton("Yes")
        self.disable_radio = QtWidgets.QRadioButton("No")
        self.enable_radio.setChecked(True)

        radio_layout = QtWidgets.QHBoxLayout()
        radio_layout.addStretch()
        radio_layout.addWidget(self.enable_radio)
        radio_layout.addWidget(self.disable_radio)
        radio_layout.addStretch()
        layout.addLayout(radio_layout)

        self.enable_radio.toggled.connect(self.toggle_audio_fields)

        # --- Image Selection ---
        label_img = QtWidgets.QLabel("Select your custom splash image:")
        label_img.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label_img)
        self.image_text = QtWidgets.QLineEdit()
        self.image_btn = QtWidgets.QPushButton("Select Image File")
        layout.addWidget(self.image_text)
        layout.addWidget(self.image_btn)
        self.image_btn.clicked.connect(self.select_image_file)

        # --- Audio Selection ---
        self.audio_label = QtWidgets.QLabel("Select your custom startup sound:")
        self.audio_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.audio_label)

        self.audio_text = QtWidgets.QLineEdit()
        self.audio_btn = QtWidgets.QPushButton("Select Audio File")
        layout.addWidget(self.audio_text)
        layout.addWidget(self.audio_btn)

        # Hide audio widgets by default
        self.audio_label.setVisible(True)
        self.audio_text.setVisible(True)
        self.audio_btn.setVisible(True)
        self.audio_btn.clicked.connect(self.select_audio_file)

        # --- Close Button ---
        self.close_btn = QtWidgets.QPushButton("Close")
        layout.addWidget(self.close_btn)
        self.close_btn.clicked.connect(self.close)

    # ---------------- UI Callbacks ----------------
    def toggle_audio_fields(self):
        if not self.ui_initialized:
            return
        visible = self.enable_radio.isChecked()
        self.audio_label.setVisible(visible)
        self.audio_text.setVisible(visible)
        self.audio_btn.setVisible(visible)
        if not visible:
            save_settings(None)
            QtWidgets.QMessageBox.information(self, "Audio Disabled", "Startup sound has been deactivated.")

    def select_image_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select PNG Image", "", "PNG Files (*.png)")
        if path:
            self.image_text.setText(os.path.basename(path))
            set_splash_screen(path, None)

    def select_audio_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select WAV Audio", "", "WAV Files (*.wav)")
        if path:
            self.audio_text.setText(os.path.basename(path))
            save_settings(path)
            QtWidgets.QMessageBox.information(self, "Success", "Audio file set successfully. Please restart Maya to hear the change.")

# ---------------- Run Loader ----------------
if __name__ == "__main__":
    dlg = SplashToolWindow(parent=maya_main_window())
    dlg.show()
