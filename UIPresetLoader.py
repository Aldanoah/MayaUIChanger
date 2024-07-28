import os
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets

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
        cmds.menuItem(label='Blender Dark', command=make_theme_changer('Blender Dark'))
        cmds.menuItem(label='Blender Light', command=make_theme_changer('Blender Light'))
        cmds.menuItem(label='Edgerunners', command=make_theme_changer('Edgerunners'))
        cmds.menuItem(label='Maya Default', command=make_theme_changer('Maya Default'))
    else:
        cmds.warning("Failed to find main Maya window.")

def run():
    create_menu()
