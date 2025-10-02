import os
import json
import maya.cmds as cmds
import maya.OpenMayaUI as omui

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtWidgets, QtCore
except ImportError:
    from shiboken6 import wrapInstance
    from PySide6 import QtWidgets, QtCore

# ---------------- Settings ----------------
settings_file_path = os.path.join(cmds.internalVar(userAppDir=True), "theme_settings.json")

def save_settings(settings):
    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

def load_settings():
    if os.path.exists(settings_file_path):
        with open(settings_file_path, 'r') as f:
            return json.load(f)
    return {}

# ---------------- Paint-driven Widgets ----------------
PAINT_DRIVEN_CLASSES = [
    "QmayaColorSliderLabel",
    "QmayaColorSliderGrp",
    "QmayaGradientControl",
    "QmayaRenderView",
    "QmayaGLWidget",
    "QmayaSwatchWidget",
    "QmayaColorEditor"
]

def clear_paint_driven_styles(widget):
    if widget is None:
        return
    for child in widget.findChildren(QtWidgets.QWidget):
        if child.metaObject().className() in PAINT_DRIVEN_CLASSES:
            child.setStyleSheet("")
            child.setAttribute(QtCore.Qt.WA_StyledBackground, False)
            child.update()
            child.repaint()

def defer_clear(widget):
    if widget is None:
        return
    QtCore.QTimer.singleShot(0, lambda: clear_paint_driven_styles(widget))

TARGET_WINDOWS = [
    "colorPreferenceWindow",
    "hyperShadePanel1Window",
    "rampNodeAttributeEditor",
    "AttributeEditor"
]

def clear_target_windows():
    for widget in QtWidgets.QApplication.topLevelWidgets():
        if isinstance(widget, QtWidgets.QWidget) and widget.objectName() in TARGET_WINDOWS:
            defer_clear(widget)
            if widget.objectName() == "colorPreferenceWindow":
                try:
                    from maya.plugin.evaluator import cache_ui
                    cache_ui.cache_ui_colour_preferences_update()
                except Exception:
                    pass
            elif widget.objectName() == "hyperShadePanel1Window":
                for child in widget.findChildren(QtWidgets.QWidget):
                    if child.metaObject().className() == "QmayaColorSliderGrp":
                        try:
                            child.updateValue()
                        except Exception:
                            child.update()

# ---------------- Event Filters ----------------
class PaintDrivenFilter(QtCore.QObject):
    """Auto-clear paint-driven styles on specific top-level windows."""
    def eventFilter(self, obj, event):
        try:
            if isinstance(obj, QtWidgets.QWidget) and event.type() == QtCore.QEvent.Show:
                if obj.objectName() in TARGET_WINDOWS:
                    defer_clear(obj)
        except Exception as e:
            print("PaintDrivenFilter error:", e)
        return QtCore.QObject.eventFilter(self, obj, event)

def install_paint_driven_filter():
    app = QtWidgets.QApplication.instance()
    if not hasattr(app, "_paint_driven_filter"):
        app._paint_driven_filter = PaintDrivenFilter(app)
        app.installEventFilter(app._paint_driven_filter)
    return app._paint_driven_filter

# ---------------- App Menu Style Filter ----------------
def extract_custom_styles(qss_text, token_name):
    """Extract blocks like myQMenu { ... }"""
    import re
    pattern = re.compile(rf"{token_name}\s*\{{(.*?)\}}", re.DOTALL)
    blocks = pattern.findall(qss_text)
    return "\n".join(block.strip() for block in blocks)

class AppMenuStyleFilter(QtCore.QObject):
    """Apply custom QMenu/QWidget styling only to menus attached to QmayaMenuBar."""
    def __init__(self, app_menu_styles="", widget_styles=""):
        super().__init__()
        self.app_menu_styles = app_menu_styles
        self.widget_styles = widget_styles

    def eventFilter(self, obj, event):
        if isinstance(obj, QtWidgets.QMenu) and event.type() == QtCore.QEvent.Show:
            parent_bar = obj.parentWidget()
            if parent_bar and parent_bar.metaObject().className() == "QmayaMenuBar":
                obj.setStyleSheet(self.app_menu_styles)
                for child in obj.findChildren(QtWidgets.QWidget):
                    child.setStyleSheet(self.widget_styles)
        return False

def install_app_menu_filter(app_menu_styles="", widget_styles=""):
    app = QtWidgets.QApplication.instance()
    if not hasattr(app, "_app_menu_filter"):
        app._app_menu_filter = AppMenuStyleFilter(app_menu_styles, widget_styles)
        app.installEventFilter(app._app_menu_filter)
    return app._app_menu_filter

# ---------------- Theme Loader ----------------
def apply_styles(selected_theme):
    maya_script_dir = os.path.join(cmds.internalVar(userScriptDir=True), "MayaUIChanger/")
    qss_file = os.path.join(maya_script_dir, f"{selected_theme.lower().replace(' ', '')}_stylesheet.qss")

    if not os.path.exists(qss_file):
        cmds.warning(f"Style file not found: {qss_file}")
        return

    with open(qss_file, "r") as file:
        style_sheet = file.read()

    # Global QSS (for most widgets)
    app = QtWidgets.QApplication.instance()
    app.setStyleSheet(style_sheet)

    # Extract custom tokens
    app_menu_styles = extract_custom_styles(style_sheet, "myQMenu")
    widget_styles = extract_custom_styles(style_sheet, "myQWidget")

    # Install event filters
    install_paint_driven_filter()
    install_app_menu_filter(app_menu_styles, widget_styles)

    clear_target_windows()

    # Save selected theme
    settings = load_settings()
    settings['selected_theme'] = selected_theme
    save_settings(settings)

# ---------------- Theme Menu ----------------
def create_menu():
    def make_theme_changer(theme):
        return lambda *args: apply_styles(theme)

    if cmds.menu('myMenu', exists=True):
        cmds.deleteUI('myMenu', menu=True)

    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr:
        wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        cmds.menu('myMenu', label='Themes', parent='MayaWindow', tearOff=True)

        for theme in [
            'Maya Default', 'Apple Pro', 'Blender Dark', 'Blender Light',
            'Edgerunners', 'easyBLUE', 'Modo', 'Umbra', 'Unreal', 'Zbrush'
        ]:
            cmds.menuItem(label=theme, command=make_theme_changer(theme))
    else:
        cmds.warning("Failed to find main Maya window.")

# ---------------- Run Loader ----------------
def run():
    create_menu()
    settings = load_settings()
    if 'selected_theme' in settings:
        apply_styles(settings['selected_theme'])

run()
