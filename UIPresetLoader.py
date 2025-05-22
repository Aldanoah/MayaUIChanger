import os
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import json

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtWidgets
except:
    from shiboken6 import wrapInstance
    from PySide6 import QtWidgets

# Defines path to settings JSON file
settings_file_path = os.path.join(cmds.internalVar(userAppDir=True), "theme_settings.json")

# Function to save user preset to a JSON file
def save_settings(settings):
    with open(settings_file_path, 'w') as f:
        json.dump(settings, f)

# Function to load user preset from a JSON file
def load_settings():
    if os.path.exists(settings_file_path):
        with open(settings_file_path, 'r') as f:
            return json.load(f)
    return {}

def apply_styles(selected_theme):
    # Get the default Maya script directory
    maya_script_dir = cmds.internalVar(userScriptDir=True) + "MayaUIChanger/"
    
    # Define the path to the chosen QSS file based on selected_theme
    qss_file = os.path.join(maya_script_dir, f"{selected_theme.lower().replace(' ', '')}_stylesheet.qss")

    if os.path.exists(qss_file):
        with open(qss_file, "r") as file:
            style_sheet = file.read()
        
        # Apply the stylesheet
        app = QtWidgets.QApplication.instance()
        app.setStyleSheet(style_sheet)
        
        # Save the settings
        settings = load_settings()
        settings['selected_theme'] = selected_theme
        save_settings(settings)
        
    else:
        cmds.warning("Style file not found: {}".format(qss_file))

def create_menu():
    # Helper function to create a theme changer command
    def make_theme_changer(theme):
        return lambda *args: apply_styles(theme)

    # Check if the menu already exists, if so, delete it
    if cmds.menu('myMenu', exists=True):
        cmds.deleteUI('myMenu', menu=True)

    # Create a new menu in the main Maya window
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        main_window = wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        # Parent the menu directly to the main Maya window
        cmds.menu('myMenu', label='Themes', parent='MayaWindow', tearOff=True)
        
        # Add new menu items that call the theme change function through the helper function
        cmds.menuItem(label='Unreal Engine', command=make_theme_changer('Unreal'))
        cmds.menuItem(label='Blender Light', command=make_theme_changer('Blender Light'))
        cmds.menuItem(label='Blender Dark', command=make_theme_changer('Blender Dark'))
        cmds.menuItem(label='Zbrush Dark', command=make_theme_changer('Zbrush'))
        cmds.menuItem(label='Easy Blue', command=make_theme_changer('easyBLUE'))
        cmds.menuItem(label='Modo Dark', command=make_theme_changer('Modo'))
        cmds.menuItem(label='Umbra Dark', command=make_theme_changer('Umbra'))
        cmds.menuItem(label='Edgerunners', command=make_theme_changer('Edgerunners'))
        cmds.menuItem(label='Maya Default', command=make_theme_changer('Maya Default'))
    else:
        cmds.warning("Failed to find main Maya window.")

def run():
    create_menu()
    # Load the last selected preset on startup
    settings = load_settings()
    if 'selected_theme' in settings:
        apply_styles(settings['selected_theme'])
run()
