import os
import sys
import shutil
import winsound
import json
import glob
import tempfile
import maya.utils

# ---------------- Qt Import ----------------
try:
    from PySide6 import QtWidgets, QtCore, QtGui
    import shiboken6 as shiboken
except ImportError:
    from PySide2 import QtWidgets, QtCore, QtGui
    import shiboken2 as shiboken

import maya.OpenMayaUI as omui

# ---------------- Settings ----------------
settings_file_path = os.path.expanduser("~/.maya_splash_settings.json")

def save_settings(audio_file_path=None, audio_enabled=False):
    settings = {
        "audio_enabled": audio_enabled
    }

    if audio_enabled and isinstance(audio_file_path, str):
        settings["audio_file"] = audio_file_path
    else:
        settings["audio_file"] = ""

    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

def load_settings():
    if os.path.isfile(settings_file_path):
        with open(settings_file_path, 'r') as f:
            return json.load(f)
    return {"audio_enabled": False, "audio_file": ""}

# ---------------- Maya Path Detection ----------------
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

# ---------------- Image Resizing ----------------
def resize_image_to_match(source_path, target_path):
    if not os.path.isfile(source_path) or not os.path.isfile(target_path):
        return source_path

    target_img = QtGui.QImage(target_path)
    source_img = QtGui.QImage(source_path).convertToFormat(QtGui.QImage.Format_ARGB32)

    if target_img.isNull() or source_img.isNull():
        return source_path

    target_size = QtCore.QSize(860, 500)

    scaled = source_img.scaled(
        target_size,
        QtCore.Qt.KeepAspectRatioByExpanding,
        QtCore.Qt.SmoothTransformation
    )

    x = (scaled.width() - target_size.width()) // 2
    y = (scaled.height() - target_size.height()) // 2

    cropped = scaled.copy(
        x,
        y,
        target_size.width(),
        target_size.height()
    )

    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(
    tempfile.gettempdir(),
    f"maya_resized_{os.getpid()}.png")

    cropped.save(temp_path, "PNG")

    return temp_path

# ---------------- Splash Handling ----------------
def set_splash_screen(image_path, text_field=None):
    if not os.path.isfile(image_path):
        QtWidgets.QMessageBox.warning(None, "Error", "File does not exist.")
        return

    maya_install_path = get_maya_install_path()
    splash_screen_path = find_splash_image_path(maya_install_path)

    splash_dir = os.path.dirname(splash_screen_path)
    backup_path = os.path.join(
        splash_dir,
        os.path.basename(splash_screen_path).replace(".png", "_backup.png")
    )

    if not os.path.isfile(backup_path) and os.path.isfile(splash_screen_path):
        shutil.copyfile(splash_screen_path, backup_path)

    resized_path = resize_image_to_match(image_path, splash_screen_path)

    try:
        shutil.copyfile(resized_path, splash_screen_path)
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Error", str(e))
        return

    if text_field:
        text_field.setText(os.path.basename(image_path))

    QtWidgets.QMessageBox.information(
        None,
        "Success",
        "Splash updated successfully.\nPlease Restart Maya."
    )

# ---------------- AUDIO ----------------
startup_sound_played = False

def get_audio_settings():
    s = load_settings()
    return s.get("audio_enabled", False), s.get("audio_file", "")

audio_enabled, audio_file = get_audio_settings()

if audio_enabled and audio_file and os.path.isfile(audio_file):
    def play_startup_sound_once():
        global startup_sound_played
        if not startup_sound_played:
            startup_sound_played = True
            try:
                winsound.PlaySound(audio_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print("Audio error:", e)

# ---------------- UI ----------------
def maya_main_window():
    ptr = omui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(int(ptr), QtWidgets.QWidget)

class SplashToolWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SplashToolWindow, self).__init__(parent)

        self.setWindowTitle("Splash Loader V2")
        self.setMinimumWidth(350)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.build_ui()
        self.load_settings_ui()

    def build_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        img_label = QtWidgets.QLabel("Select Splash Image:")
        img_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(img_label)

        self.image_text = QtWidgets.QLineEdit()
        self.image_btn = QtWidgets.QPushButton("Browse Image")
        layout.addWidget(self.image_text)
        layout.addWidget(self.image_btn)

        self.image_btn.clicked.connect(self.select_image)

        self.enable_audio = QtWidgets.QCheckBox("Enable Startup Sound")
        layout.addWidget(self.enable_audio)

        self.audio_text = QtWidgets.QLineEdit()
        self.audio_btn = QtWidgets.QPushButton("Browse Audio")

        layout.addWidget(self.audio_text)
        layout.addWidget(self.audio_btn)

        self.audio_btn.clicked.connect(self.select_audio)

        self.enable_audio.toggled.connect(self.toggle_audio)

        close_btn = QtWidgets.QPushButton("Close")
        layout.addWidget(close_btn)
        close_btn.clicked.connect(self.close)

    # ---------------- SETTINGS UI ----------------
    def load_settings_ui(self):
        s = load_settings()
        enabled = s.get("audio_enabled", False)
        self.enable_audio.setChecked(enabled)
        self.audio_text.setText(s.get("audio_file", ""))

        self.toggle_audio(enabled)

    def toggle_audio(self, state):
        self.audio_text.setEnabled(state)
        self.audio_btn.setEnabled(state)

        if not state:
            save_settings(audio_file_path=None, audio_enabled=False)

    # ---------------- ACTIONS ----------------
    def select_image(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if path:
            self.image_text.setText(path)
            set_splash_screen(path, self.image_text)

    def select_audio(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Audio", "", "WAV Files (*.wav)"
        )
        if path:
            self.audio_text.setText(path)

            save_settings(
                audio_file_path=path,
                audio_enabled=self.enable_audio.isChecked()
            )

# ---------------- RUN ----------------
def run():
    global splash_window

    try:
        splash_window.close()
        splash_window.deleteLater()
    except:
        pass

    splash_window = SplashToolWindow(parent=maya_main_window())
    splash_window.show()

if __name__ == "__main__":
    run()