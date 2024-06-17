import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets, QtCore

# Start of Functions
def on_theme_change(theme):
    change_interface_color(theme)

def change_interface_color(selected_object):
    # Get main Maya window
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        main_window = wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        apply_stylesheet_recursive(main_window, selected_object)
    else:
        print("Failed to find main Maya window.")
 
def cycle_background_color_to_black():
    # Set the background color to black
    cmds.displayRGBColor('background', 0, 0, 0)
    cmds.displayRGBColor('backgroundTop', 0, 0, 0)
    cmds.displayRGBColor('backgroundBottom', 0, 0, 0)

    # Apply changes to all model panels
    model_panels = cmds.getPanel(type="modelPanel")
    for panel in model_panels:
        if cmds.modelEditor(panel, query=True, exists=True):
            cmds.modelEditor(panel, edit=True, displayAppearance='smoothShaded')

def cycle_background_color_to_light_grey():
    # Set the background color to light grey 
    light_grey = 0.4
    cmds.displayRGBColor('background', light_grey, light_grey, light_grey)
    cmds.displayRGBColor('backgroundTop', light_grey, light_grey, light_grey)
    cmds.displayRGBColor('backgroundBottom', light_grey, light_grey, light_grey)

    # Apply changes to all model panels
    model_panels = cmds.getPanel(type="modelPanel")
    for panel in model_panels:
        if cmds.modelEditor(panel, query=True, exists=True):
            cmds.modelEditor(panel, edit=True, displayAppearance='smoothShaded')

def apply_stylesheet_recursive(widget, selected_object):
    if isinstance(widget, QtWidgets.QWidget):
        if selected_object == "Blender Dark":
            widget.setStyleSheet("""
                
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget { background-color: #404040; color: #e6e6e6; selection-color: rgb(254,254,254); selection-background-color: rgb(86,128,194); font-family: DejaVuSans; font-size: 12px; }
                
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox { background-color: #2c2c2c; border: 1px solid #404040; padding-left: 6px; border-radius: 0.2em; }
                QComboBox:on { background-color: #5680c2; color: #f8f9f9;}
                QComboBox:disabled  { background-color: #323232; color: #8a8a8a; }
                QComboBox::down-arrow { image: url('D:/Maya/Scripts/Images/Arrow-204-16.ico'); width: 8px; height: 8px; }
                QComboBox::drop-down { width: 15px; border-radius: 0.2em; border-left-width: 0px; }
                QComboBox QAbstractItemView { border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; selection-background-color: #5680c2; }
                
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenu { background-color: rgb(82,82,82); }
                QMenu::item { background-color: transparent; spacing: 3px; padding: 3px 15px; }
                QMenu::separator { height:0px; margin-left:5px; margin-right:5px; } 

                /*-----QMenuBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar { background-color: transparent; spacing:2px; }
                QMenuBar::item { color: rgb(193,193,193); }
                QMenuBar::item:selected { color: rgb(225,225,225); background-color: rgb(94,132,191); border-style: outset; border-radius: 0.2em; }
                
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabBar::tab { background-color: #373737; border-style: solid; border-width: 1px; border-top-color: #373737; border-right-color: #373737; border-left-color: #373737; border-bottom-color: #373737; padding: 5px; }
                QTabBar::tab:selected { background-color: #424242; border-style: solid; border-width: 1px; border-color: #373737; border-bottom-color: #424242; }
                QTabBar::tab:!selected { border-style: solid; border-width: 1px; background-color: #2c2c2c; color: #d8d8d8; }
                QTabBar::tab:hover:!selected { background-color: #343434; color: #afafaf; }
                QTabBar::tab:last { border-top-right-radius: 0em; margin-right: 0; }
                
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabWidget::pane { background-color: #2c2c2c; }
                
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QTextEdit { color: rgb(149, 214, 000); background-color: rgb(29,29,29); }
                QTextEdit:!editable { background-color: rgb(29,29,29); }
                                 
                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/           
                QSlider { background-color: rgb(84,84,84); }
                QSlider::handle { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd); border: 1px solid #444; }
                QSlider::handle:horizontal:hover { background: rgb(71,114,179); border-radius: 0px; }
                QSlider::handle:horizontal:disabled { background: #eee; border: 1px solid #aaa; border-radius: 4px; }
                QSlider::sub-page:horizontal { background: rgb(71,114,179); }
                QSlider::add-page:horizontal:disabled { background: rgb(40,40,40); border-color: #999; }
                
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QCheckBox { background-color: transparent; color: #e4e4d4; } 
                QCheckBox::indicator { width: 12px; height: 12px; }   
                QCheckBox::indicator:checked { image: url('D:/Maya/Scripts/Images/checkmark-16.ico'); background-color: rgb(71,114,179); border-radius: 0.2em; }    
                QCheckBox::indicator:unchecked { background-color: rgb(84,84,84); border-radius: 0.2em; }
                QCheckBox::indicator:unchecked:hover { color: #f5f5f5; }
                
                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QRadioButton { background: transparent; color: #e4e4d4; }
                QRadioButton::indicator { width: 12px; height: 12px; }
                
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QLineEdit { color: #dcdcdc; background-color: #2c2c2c; border: 1px solid #404040; border-color: rgb(61,61,61); border-radius: 0.3em; padding: 0px; }
                
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/           
                QLabel { color:#e6e6e6; background-color: transparent; }
                
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QProgressBar { background-color: #424242; border: 1px solid #373737; padding: 0px; text-align: right; } 
                QProgressBar::chunk { background-color: #5680c2; border: 1px solid #373737; }
                
                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QMessageBox { color: rgb(40,40,40); background-color: rgb(24,24,24); }
                QMessageBox QPushButton { min-width: 105px; }
                
                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QPushButton { background-color: transparent; border: 1px solid #404040; }
                QPushButton:default { background-color: #5379b4; }    
                QPushButton:disabled { background-color: #323232; color: #8a8a8a; }     
                QPushButton:hover { background-color: #676767; }   
                QPushButton:pressed { background-color: #5680c2; color:#fcfdfd; }

                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QGroupBox { border: 0px solid #373737; background-color: #373737; padding-top: 12px; }
                QGroupBox::title { background-color: transparent; margin-top: 4px; padding-left: 8px; }
                
                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/           
                QHeaderView { background-color: #3b3b3b; border: 0px transparent transparent; }
                QHeaderView:section { background-color: #3b3b3b; border: 0px transparent transparent; }
                
                /*-----QListView------------------------------------------------------------------------------------------------------------------------------------*/           
                QListView { background-color: #232323; border: 0px transparent transparent; }
                QListView:disabled { background-color: #19232D; color: #787878; }
                QListView:item { background-color: #282828; }
                QListView:item:hover { background-color: #484848; border: 0px transparent transparent; }
                QListView:item:selected { background-color: #314e78; border: 0px transparent transparent; color: #c68652; }

                /*-----QSpinBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QSpinBox { background: #595959; border: 1px solid #404040; text-align: center; }
                QSpinBox::down-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top left; width: 13px; height: 20px; }
                QSpinBox::down-button:hover { background:#6b6b6b; }   
                QSpinBox::hover { background: #808080; }
                QSpinBox::up-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top right; width: 13px; height: 20px; }    
                QSpinBox::up-button:hover { background:#6b6b6b; }
                
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/           
                QTableView QTableCornerButton:section { background-color: #3b3b3b; border: 1px solid #3b3b3b; }
                
                /*-----QTreeView-----------------------------------------------------------------------------------------------------------------------------------*/           
                QTreeView { background-color: #232323; border: 0px transparent transparent; }
                QTreeView:disabled { background-color: #19232D;  color: #787878; }
                QTreeView:item { background-color: #282828; }
                QTreeView:item:hover { background-color: #484848; border: 0px transparent transparent; }
                QTreeView:item:selected { background-color: #314e78; border: 0px transparent transparent; color: #c68652; }
                                       
            """)

            # Change viewport display color to light grey
            cycle_background_color_to_light_grey()
        elif selected_object == "Blender Light":
            widget.setStyleSheet("""
                QWidget { background-color: rgb(192, 192, 192); color: rgb(216,216,216); }
                QComboBox { color: rgb(216,216,216); background-color: rgb(59,59,59); }
                QMenuBar::item:selected { color: rgb(225,225,225); background-color: rgb(94,132,191); }
            """)
            cycle_background_color_to_black()

# Start of UI
winName = "Maya UI Changer"
if cmds.window(winName, q=True, ex=True):
    cmds.deleteUI(winName)
cmds.window(winName)

form = cmds.formLayout()
title = cmds.text(label="Maya UI Changer", align="center", height=30)

themes = ["Blender Dark", "Blender Light"]
icon_paths = {
    "Blender Dark": "D:/Maya/Scripts/Images/Blender_logo_1.png",
    "Blender Light": "D:/Maya/Scripts/Images/Blender_logo_2.png",  
}

buttons = []
for theme in themes:
    icon_path = icon_paths.get(theme, "")
    button = cmds.iconTextButton(
        style='iconAndTextVertical',
        image1=icon_path,
        label=theme,
        command=lambda t=theme: on_theme_change(t)
    )
    buttons.append(button)

spacing = 10
button_width = 50
button_height = 50

cmds.formLayout(form, edit=True, attachForm=[
    (title, 'top', 10), (title, 'left', 10), (title, 'right', 10),
    (buttons[0], 'top', 50), (buttons[0], 'left', 10)
])

for i in range(1, len(buttons)):
    cmds.formLayout(form, edit=True, attachForm=[
        (buttons[i], 'top', 50)
    ], attachControl=[
        (buttons[i], 'left', spacing, buttons[i-1])
    ], width=button_width, height=button_height)

cmds.setParent('..')
cmds.showWindow()

# Highlight on hover for buttons
for button in buttons:
    widget = wrapInstance(int(omui.MQtUtil.findControl(button)), QtWidgets.QWidget)
    widget.setStyleSheet("QPushButton:hover { border: 2px solid white; }")
