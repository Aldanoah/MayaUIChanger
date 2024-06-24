import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets

# Triggers the change interface function.
def on_theme_change(theme):
    change_interface_color(theme)

# Function to create a Menu 
def create_menu():
    # Helper function to trigger the theme change function 
    def make_theme_changer(theme):
        def theme_changer(*args):
            on_theme_change(theme)
        return theme_changer

    # Check if the menu already exists, if so, delete it
    if cmds.menu('myMenu', exists=True):
        cmds.deleteUI('myMenu', menu=True)

    # Create a new menu in the main Maya window
    cmds.menu('myMenu', label='Themes', parent='MayaWindow', tearOff=True)
    
   # Add new menu items that call the theme change function through the helper function
    cmds.menuItem(label='Blender Dark', command=make_theme_changer('Blender Dark'))
    cmds.menuItem(label='Blender Light', command=make_theme_changer('Blender Light'))
    cmds.menuItem(label='Edgerunners', command=make_theme_changer('Edgerunners'))
    cmds.menuItem(label='Maya Default', command=make_theme_changer('Maya Default'))
create_menu()

def change_interface_color(selected_object):

    #   Function to find Maya's top level window to enable recursive application of the stylesheet.
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        main_window = wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        apply_stylesheet_recursive(main_window, selected_object)
    else:
        print("Failed to find main Maya window.")

def cycle_background_color_to_black():
    
    #Set the background color to black and apply the changes to all model panels.
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

# Function to recursively apply the custom stylesheet presets.
def apply_stylesheet_recursive(widget, selected_object):
    if isinstance(widget, QtWidgets.QWidget):
        if selected_object == "Blender Dark":
            widget.setStyleSheet("""
                
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget { background-color: #404040; color: #e6e6e6; selection-color: rgb(254,254,254); selection-background-color: rgb(86,128,194); font-family: DejaVu Sans Condensed; font-size: 12px; font-weight: normal; }
                
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox { background-color: #2c2c2c; border: 1px solid #404040; padding-left: 6px; border-radius: 0.2em; }
                QComboBox:on { background-color: rgb(67,97,143); color: #f8f9f9;}
                QComboBox:disabled  { background-color: #323232; color: #8a8a8a; }
                QComboBox::down-arrow { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/Arrow-204-16.ico'); width: 8px; height: 8px; }
                QComboBox::drop-down { width: 15px; border-radius: 0.2em; border-left-width: 0px; }
                QComboBox QAbstractItemView { border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; selection-background-color: #5680c2; }
                
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenu { background-color: transparent; }
                QMenu::item { background-color: transparent; spacing: 3px; padding: 3px 15px; }
                QMenu::separator { height:0px; margin-left:5px; margin-right:5px; } 

                /*-----QMenuBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar { background-color: transparent; spacing:2px; padding-top: 2px; }
                QMenuBar::item { color: rgb(193,193,193); }
                QMenuBar::item:selected { color: rgb(225,225,225); background-color: rgb(94,132,191); border-style: outset; border-radius: 0.2em; }
                
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabBar::tab { background-color: #373737; border-style: solid; border-width: 1px; border-top-color: #373737; border-right-color: #373737; border-left-color: #373737; border-bottom-color: #373737; padding: 5px 10px 3px 10px; border-top-left-radius: 0.3em; border-top-right-radius: 0.3em; border-bottom-style: solid; }
                QTabBar::tab:selected { background-color: #424242; border-style: solid; border-width: 1px; border-color: #373737; border-bottom-color: #424242; }
                QTabBar::tab:!selected { border-style: solid; border-width: 1px; background-color: #2c2c2c; color: #d8d8d8; }
                QTabBar::tab:hover:!selected { background-color: #343434; color: #afafaf; }
                QTabBar::tab:last { border-top-right-radius: 0.3em; margin-right: 0; }
                
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabWidget::pane { background-color: #404040; }
                
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QTextEdit { color: rgb(149, 214, 000); background-color: rgb(29,29,29); }
                QTextEdit:!editable { background-color: rgb(29,29,29); }
                                 
                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/           
                QSlider { background-color: rgb(84,84,84); border: 1px solid; border-color: #373737; border-radius: 0.3em; }
                QSlider:hover { background-color: rgb(101,101,101); }
                QSlider::handle { background: transparent; }
                QSlider::handle:horizontal:disabled { background: #eee; border: 1px solid #aaa; border-radius: 4px; }
                QSlider::sub-page:horizontal { background: rgb(71,114,179); }
                QSlider::add-page:horizontal:disabled { background: rgb(40,40,40); border-color: #999; }
                
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QCheckBox { background-color: transparent; color: #e4e4d4; } 
                QCheckBox::indicator { width: 13px; height: 13px; }   
                QCheckBox::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked.png'); } 
                QCheckBox::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked_hover.png'); }   
                QCheckBox::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked.png'); }
                QCheckBox::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked_hover.png'); }

                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QRadioButton { background: transparent; color: #e4e4d4; }
                QRadioButton::indicator { width: 10px; height: 10px; }
                QRadioButton::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked.png'); }
                QRadioButton::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked_hover.png'); }
                QRadioButton::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked.png'); }
                QRadioButton::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked_hover.png'); }
                                 
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QLineEdit { color: #dcdcdc; background-color: #2c2c2c; border: 1px solid #404040; border-color: rgb(61,61,61); border-radius: 0.3em; padding: 0px; }
                
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/           
                QLabel { color:#e6e6e6; background-color: transparent; }
                
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QProgressBar { background-color: #424242; border: 1px solid #373737; padding: 0px; text-align: right; } 
                QProgressBar::chunk { background-color: #5680c2; border: 1px solid #373737; }
                
                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QMessageBox { color: rgb(229,229,229); background-color: rgb(24,24,24); }
                QMessageBox QPushButton { min-width: 105px; min-height: 20px; background-color: rgb(84,84,84); border-radius: 0.2em; } 
                QMessageBox QPushButton:hover { color: rgb(234,240,248); background-color: rgb(101,101,101);} 
                QMessageBox QPushButton:default:hover { color: rgb(234,240,248); background-color: rgb(121,158,215); }                                             
                
                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QPushButton { background-color: rgb(84,84,84);  border: 1px solid #404040; border-radius: 0.3em; }
                QPushButton:default { background-color: #5379b4; }    
                QPushButton:disabled { background-color: #323232; color: #8a8a8a; }     
                QPushButton:hover { background-color: rgb(101,101,101); }   
                QPushButton:pressed { background-color: #5680c2; color:#fcfdfd; }

                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QGroupBox { border: 0px solid #373737; background-color: rgb(40,40,40);  padding-top: 12px; }
                QGroupBox::title { background-color: transparent; margin-top: 4px; padding-left: 8px; }
                
                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/           
                QHeaderView { background-color: #3b3b3b; border: 0px transparent transparent; }
                QHeaderView:section { color: #f8f9f9; background-color: #3b3b3b; border: 0px transparent transparent; }
                
                /*-----QListView------------------------------------------------------------------------------------------------------------------------------------*/           
                QListView { background-color: rgb(40,40,40); border: 0px transparent transparent; }
                QListView:disabled { background-color: #19232D; color: #787878; }
                QListView:item { background-color: transparent; }
                QListView:item:hover { background-color: rgb(63,63,63); border: 0px transparent transparent; }
                QListView:item:selected { background-color: rgb(61,89,132); border: 0px transparent transparent; }
                QListView:item:disabled { color: rgb(135,135,135); border: 0px transparent transparent; }

                /*-----QSpinBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QSpinBox { background: #595959; border: 1px solid #404040; text-align: center; }
                QSpinBox::down-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top left; width: 13px; height: 20px; }
                QSpinBox::down-button:hover { background:#6b6b6b; }   
                QSpinBox::hover { background: #808080; }
                QSpinBox::up-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top right; width: 13px; height: 20px; }    
                QSpinBox::up-button:hover { background:#6b6b6b; }
                
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/           
                QTableView { color: rgb(153,153,153); background-color: rgb(40,40,40); border: 1px solid #3b3b3b; }
                QTableView QTableCornerButton:section { background-color: #3b3b3b; border: 1px solid #3b3b3b; }
                
                /*-----QTreeView-----------------------------------------------------------------------------------------------------------------------------------*/           
                QTreeView { background-color: #232323; border: 0px transparent transparent; }
                QTreeView:disabled { background-color: #19232D;  color: #787878; }
                QTreeView:item:hover { background-color: #484848; border: 0px transparent transparent; }
                QTreeView:item:selected { background-color: #314e78; border: 0px transparent transparent; color: #c68652; }
                                 
                /*-----QScrollBar-----------------------------------------------------------------------------------------------------------------------------------*/           
                QScrollBar:vertical { border: 0px; background-color: rgb(84,84,84); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar:horizontal { border: 0px; background-color: rgb(84,84,84); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar::handle:vertical { min-height: 0px; border: 0px; background-color: rgb(84,84,84); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::handle:horizontal { min-height: 0px; border: 0px; background-color: rgb(84,84,84); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::add-line:vertical { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::add-line:horizontal { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::sub-line:vertical { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                QScrollBar::sub-line:horizontal { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                                       
            """)

            # Change viewport display color to light grey
            cycle_background_color_to_light_grey()

        elif selected_object == "Blender Light":
            widget.setStyleSheet("""

                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget { background-color: rgb(166,166,166); color: rgb(216,216,216); selection-color: rgb(254,254,254); selection-background-color: rgb(86,128,194); font-family: DejaVu Sans Condensed; font-size: 12px; font-weight: normal; }
                                 
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox { background-color: rgb(59,59,59); color: rgb(216,216,216); border: 1px solid #404040; padding-left: 6px; border-radius: 0.2em; selection-background-color: rgb(192,192,192);  }
                QComboBox:on { background-color: rgb(118,118,118); color: rgb(216,216,216); }
                QComboBox:disabled  { background-color: #323232; color: #8a8a8a; }
                QComboBox::down-arrow { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/Arrow-204-16.ico'); width: 8px; height: 8px; }
                QComboBox::drop-down { width: 15px; border-radius: 0.2em; border-left-width: 0px; }
                QComboBox QAbstractItemView { background-color: rgb(59,59,59); border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; selection-background-color: rgb(5,5,5); }
    
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenu { background-color: transparent; }
                QMenu::item { background-color: transparent; spacing: 3px; padding: 3px 15px; }
                QMenu::separator { height:0px; margin-left:5px; margin-right:5px; }

                /*-----QMenuBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar { background-color: transparent; spacing:2px; padding-top: 2px; }
                QMenuBar::item { color: rgb(28,28,28); }
                QMenuBar::item:selected { color: rgb(225,225,225); background-color: rgb(94,132,191); border-style: outset; border-radius: 0.3em; }
                                 
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabBar::tab { border-style: solid; border-width: 1px; border-top-color: #373737; border-right-color: #373737; border-left-color: #373737; border-bottom-color: #373737; padding: 5px 10px 3px 10px; border-top-left-radius: 0.3em; border-top-right-radius: 0.3em; border-bottom-style: solid; }
                QTabBar::tab:selected { color: rgb(28,28,28); background-color: rgb(179,179,179); border-style: solid; border-width: 1px; border-color: #373737; border-bottom-color: #424242; }
                QTabBar::tab:!selected { color: rgb(28,28,28); border-style: solid; border-width: 1px; background-color: rgb(139,139,139); color: (33,33,33); }
                QTabBar::tab:hover:!selected { background-color: rgb(146,146,146); color: rgb(33,33,33); }
                QTabBar::tab:last { border-top-right-radius: 0.3em; margin-right: 0; }
                                                                  
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabWidget::pane { background-color: rgb(166,166,166); }
                                 
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QTextEdit { color: rgb(149, 214, 000); background-color: rgb(28,28,28); }
                QTextEdit:!editable { background-color: rgb(28,28,28); }
                                 
                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/           
                QSlider { background-color: rgb(151,151,151); border-style: solid; border: 1px solid; border-color: #373737; border-radius: 0.3em; }
                QSlider:hover { background-color: rgb(167,167,167); }
                QSlider::handle { background: transparent; }
                QSlider::handle:horizontal:disabled { background: #eee; border: 1px solid #aaa; border-radius: 4px; }
                QSlider::sub-page:horizontal { background: rgb(228,228,228); }
                QSlider::add-page:horizontal:disabled { background: rgb(40,40,40); border-color: #999; }
                                                                      
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QCheckBox { background-color: transparent; color: rgb(28,28,28); } 
                QCheckBox::indicator { width: 13px; height: 13px; }   
                QCheckBox::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked.png'); } 
                QCheckBox::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked_hover.png'); }   
                QCheckBox::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked.png'); }
                QCheckBox::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked_hover.png'); }
                                 
                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QRadioButton { background: transparent; color: rgb(28,28,28); }
                QRadioButton::indicator { width: 10px; height: 10px; }
                QRadioButton::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked.png'); }
                QRadioButton::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked_hover.png'); }
                QRadioButton::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked.png'); }
                QRadioButton::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked_hover.png'); }
                                 
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QLineEdit { color: #dcdcdc; background-color: #2c2c2c; border: 1px solid #404040; border-color: rgb(61,61,61); border-radius: 0.3em; padding: 0px; }
                 
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/           
                QLabel { color: rgb(26,26,26); background-color: transparent; }   
                                 
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QProgressBar { background-color: #424242; border: 1px solid #373737; padding: 0px; text-align: right; } 
                QProgressBar::chunk { background-color: #5680c2; border: 1px solid #373737; }

                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QMessageBox { color: rgb(40,40,40); background-color: rgb(192,192,192); }
                QMessageBox QPushButton { min-width: 105px; min-height: 20px; background-color: rgb(219,219,219); border-radius: 0.2em; } 
                QMessageBox QPushButton:hover { color: rgb(40,40,40); background-color: rgb(241,241,241);} 
                QMessageBox QPushButton:default:hover { color: rgb(234,240,248); background-color: rgb(121,158,215); } 
                                 
                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QPushButton { color: rgb(31,31,31); background-color: rgb(219,219,219); border: 1px solid #404040; border-radius: 0.3em; }
                QPushButton:default { background-color: #5379b4; color: rgb(234,240,248); }    
                QPushButton:disabled { background-color: #323232; color: #8a8a8a; }     
                QPushButton:hover { background-color: rgb(241,241,241); }   
                QPushButton:pressed { background-color: #5680c2; color: rgb(254,254,254); }
                                 
                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QGroupBox { border: 0px solid #373737; background-color: #373737; padding-top: 12px; }
                QGroupBox::title { background-color: transparent; margin-top: 4px; padding-left: 8px; }
                                 
                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/           
                QHeaderView { background-color: #3b3b3b; border: 0px transparent transparent; }
                QHeaderView:section { color: rgb(159,159,159); background-color: #3b3b3b; border: 0px transparent transparent; }
                                 
                /*-----QListView------------------------------------------------------------------------------------------------------------------------------------*/           
                QListView { background-color: rgb(59,59,59); color: rgb(216,216,216); border: 0px transparent transparent; }
                QListView:disabled { background-color: #19232D; color: #787878; }
                QListView:item { background-color: transparent; }
                QListView:item:hover { background-color: rgb(176,176,176); color: rgb(59,59,59); border: 0px transparent transparent; }
                QListView:item:selected { background-color: rgb(111,138,182); border: 0px transparent transparent; }
                QListView:item:disabled { color: rgb(138,138,138); border: 0px transparent transparent; }
                                 
                /*-----QSpinBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QSpinBox { background: #595959; border: 1px solid #404040; text-align: center; }
                QSpinBox::down-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top left; width: 13px; height: 20px; }
                QSpinBox::down-button:hover { background:#6b6b6b; }   
                QSpinBox::hover { background: #808080; }
                QSpinBox::up-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top right; width: 13px; height: 20px; }    
                QSpinBox::up-button:hover { background:#6b6b6b; }
                                 
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/           
                QTableView { color: rgb(153,153,153); background-color: rgb(153,153,153); border: 1px solid #3b3b3b; }
                QTableView QTableCornerButton:section { background-color: #3b3b3b; border: 1px solid #3b3b3b; }
                                 
                /*-----QTreeView-----------------------------------------------------------------------------------------------------------------------------------*/           
                QTreeView { color: rgb(28,28,28); background-color: rgb(153,153,153); border: 0px transparent transparent; }
                QTreeView:disabled { background-color: #19232D;  color: #787878; }
                QTreeView:item:hover { background-color: rgb(176,176,176); border: 0px transparent transparent; }
                QTreeView:item:selected { background-color: rgb(111,138,182); border: 0px transparent transparent; color: #c68652; }

                /*-----QScrollBar-----------------------------------------------------------------------------------------------------------------------------------*/           
                QScrollBar:vertical { border: 0px; background-color: rgb(228,228,228); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar:horizontal { border: 0px; background-color: rgb(228,228,228); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar::handle:vertical { min-height: 0px; border: 0px; background-color: rgb(228,228,228); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::handle:horizontal { min-height: 0px; border: 0px; background-color: rgb(228,228,228); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::add-line:vertical { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::add-line:horizontal { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::sub-line:vertical { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                QScrollBar::sub-line:horizontal { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                                                                                                          
            """)

            cycle_background_color_to_black()

        elif selected_object == "Edgerunners":
            widget.setStyleSheet("""

                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget { background-color: rgb(30,30,50); color: rgb(94,246,255); selection-color: rgb(94,246,255); selection-background-color: rgb(247,80,70); font-family: rajdhani; font-size: 13px; font-weight: bold; }
               
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox { color: rgb(29,237,131); background-color: rgb(0,0,0); border: 1px solid rgb(29, 237, 131); padding-left: 6px; border-radius: 0.2em; }
                QComboBox:on { background-color: rgb(123,39,39); color: rgb(94,246,255); }
                QComboBox:disabled  { background-color: rgb(14,11,18); color: rgb(123,39,39); border: 1px solid rgb(123,39,39); }
                QComboBox:hover,QPushButton:hover { border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0W, y2: 1, stop: 0 #f75049, stop: 1 #f75049); }
                QComboBox::down-arrow { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/Arrow-204-16.ico'); width: 8px; height: 8px; }
                QComboBox::drop-down { width: 15px; border-radius: 0.2em; border-left-width: 0px; }
                QComboBox QAbstractItemView { color: rgb(94,246,255); border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; selection-background-color: rgb(247,80,70); }
                                 
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenu { background-color: transparent; }
                QMenu::item { background-color: transparent; spacing: 3px; padding: 3px 15px; }
                QMenu::separator { height:0px; margin-left:5px; margin-right:5px; }
                                 
                /*-----QMenuBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar { background-color: transparent; spacing:2px; padding-top: 2px; border: 1px; }
                QMenuBar::item { background-color: transparent;}
                QMenuBar::item:selected { color: rgb(29, 237, 131); background-color: rgb(0,0,0); border-style: outset; border-radius: 0.2em;  }
                                 
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabBar::tab { border-width: 1px; padding: 5px 10px 3px 10px; border-top-left-radius: 0.3em; border-top-right-radius: 0.3em; border-bottom-style: solid; }
                QTabBar::tab:selected { color: rgb(94,246,255); background-color: rgb(14,11,18); border-style: solid; border-width: 1px; }
                QTabBar::tab:!selected { background-color: rgb(14,11,18); color: rgb(29,237,131); }
                QTabBar::tab:hover:!selected { background-color: rgb(123,39,39); color: rgb(94,246,255); }
                QTabBar::tab:last { border-top-right-radius: 0.3em; margin-right: 0; }
                                 
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/           
                QTabWidget::pane { background-color: rgb(14,11,18);}
                                 
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QTextEdit { color: rgb(255,255,255); background-color: rgb(14,11,18); }
                QTextEdit:!editable { background-color: rgb(14,11,18); }
                                 
                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/           
                QSlider { background-color: rgb(14,11,18); border-radius: 0.3em; }
                QSlider:hover { background-color: rgb(14,11,18); }
                QSlider::handle { background-color: rgb(94,246,255); border: 1px; }
                QSlider::handle:horizontal:disabled { background: rgb(14,11,18); border: 0px solid #aaa; }
                QSlider::sub-page:horizontal { background: rgb(247,80,70); }
                QSlider::sub-page:horizontal:disabled { background: rgb(123,39,39); }
                QSlider::add-page:horizontal:disabled { background: rgb(40,40,40); border-color: #999; }
                                 
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QCheckBox { background-color: transparent; color: #e4e4d4; } 
                QCheckBox::indicator { width: 13px; height: 13px; }   
                QCheckBox::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked.png'); } 
                QCheckBox::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_checked_hover.png'); }   
                QCheckBox::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked.png'); }
                QCheckBox::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QCheckBox_unchecked_hover.png'); }
                                 
                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QRadioButton { background: transparent; color: #e4e4d4; }
                QRadioButton::indicator { width: 10px; height: 10px; }
                QRadioButton::indicator:checked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked.png'); }
                QRadioButton::indicator:checked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_checked_hover.png'); }
                QRadioButton::indicator:unchecked { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked.png'); }
                QRadioButton::indicator:unchecked:hover { image: url('C:/Users/chine/Onedrive/Documents/maya/scripts/MayaUIChanger/Images/QRadioButton_unchecked_hover.png'); }
                                 
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/           
                QLineEdit { color: rgb(29,237,131); background-color: rgb(14,11,18); border-radius: 0.3em; padding: 0px; }
                 
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/           
                QLabel { color: #e4e4d4; background-color: transparent; }    

                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/           
                QProgressBar { background-color: #424242; border: 1px solid #373737; padding: 0px; text-align: right; } 
                QProgressBar::chunk { background-color: #5680c2; border: 1px solid #373737; } 

                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QMessageBox { color: rgb(94,246,255); background-color: rgb(14,11,18); }
                QMessageBox QPushButton { min-width: 105px; min-height: 20px; color: rgb(29, 237, 131); background-color: rgb(14,11,18); border: 1px solid rgb(29, 237, 131); border-radius: 0.2em; } 
                QMessageBox QPushButton:hover { color: rgb(94,246,255); } 
                QMessageBox QPushButton:default:hover { border: 1px solid rgb(247,80,70); } 

                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/           
                QPushButton { color: rgb(29, 237, 131); background-color: rgb(30,30,50); border: 1px solid rgb(94,246,255); border-radius: 0.3em;  }
                QPushButton:default { background-color: rgb(14,11,18); color: rgb(94,246,255); border: 1px solid rgb(94,246,255); }    
                QPushButton:disabled { background-color: rgb(123,39,39); color: rgb(94,246,255); }     
                QPushButton:hover { background-color: transparent; }   
                QPushButton:pressed { background-color: rgb(123,39,39); } 
                
                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QGroupBox { border: 0px solid #373737; background-color: rgb(14,11,18); padding-top: 12px; }
                QGroupBox::title { background-color: transparent; margin-top: 4px; padding-left: 8px; }   
                
                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/           
                QHeaderView { background-color: rgb(30,30,50); border: 0px transparent transparent; }
                QHeaderView:section { color: rgb(94,246,255); background-color: rgb(30,30,50); border: 0px transparent transparent; }    
                
                /*-----QListView------------------------------------------------------------------------------------------------------------------------------------*/           
                QListView { color: rgb(94,246,255); background-color: rgb(14,11,18); border: 0px transparent transparent; }
                QListView:disabled { background-color: #19232D; color: #787878; }
                QListView:item { background-color: transparent; }
                QListView:item:hover { background-color: rgb(123,39,39); color: rgb(94,246,255); border: 0px transparent transparent; }
                QListView:item:selected { color: rgb(94,246,255); background-color: rgb(14,11,18); border: 0px transparent transparent; }
                QListView:item:disabled { color: rgb(138,138,138); border: 0px transparent transparent; }
                
                /*-----QSpinBox------------------------------------------------------------------------------------------------------------------------------------*/           
                QSpinBox { background: #595959; border: 1px solid #404040; text-align: center; }
                QSpinBox::down-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top left; width: 13px; height: 20px; }
                QSpinBox::down-button:hover { background:#6b6b6b; }   
                QSpinBox::hover { background: #808080; }
                QSpinBox::up-button { border-width: 0px; padding-top: 3px; subcontrol-origin: control; subcontrol-position: top right; width: 13px; height: 20px; }    
                QSpinBox::up-button:hover { background:#6b6b6b; }
                
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/           
                QTableView { background-color: rgb(14,11,18); color: rgb(29,237,131); border: 1px solid #3b3b3b; }
                QTableView QTableCornerButton:section { background-color: rgb(30,30,50); border: 1px solid #3b3b3b; }
                
                /*-----QTreeView-----------------------------------------------------------------------------------------------------------------------------------*/           
                QTreeView { color: rgb(94,246,255); background-color: rgb(14,11,18); border: 0px transparent transparent; }
                QTreeView:disabled { background-color: #19232D;  color: #787878; }
                QTreeView:item:hover { background-color: rgb(176,176,176); border: 0px transparent transparent; }
                QTreeView:item:selected { color: rgb(94,246,255); background-color: rgb(14,11,18); border: 0px transparent transparent; color: #c68652; }
                
                /*-----QScrollBar-----------------------------------------------------------------------------------------------------------------------------------*/           
                QScrollBar:vertical { border: 0px; background-color: rgb(247,80,70); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar:horizontal { border: 0px; background-color: rgb(247,80,70); width:10px; margin: 0px 0px 0px 0px; }
                QScrollBar::handle:vertical { min-height: 0px; border: 0px; background-color: rgb(247,80,70); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::handle:horizontal { min-height: 0px; border: 0px; background-color: rgb(247,80,70); border-radius: 4px; border-radius: 0.3em;}
                QScrollBar::add-line:vertical { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::add-line:horizontal { height: 0px; subcontrol-position: bottom; subcontrol-origin: margin; }
                QScrollBar::sub-line:vertical { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                QScrollBar::sub-line:horizontal { height: 0px; subcontrol-position: top; subcontrol-origin: margin; }
                     
                                 
            """)

            # Change viewport display color to black
            cycle_background_color_to_black()

        elif selected_object == "Maya Default":
            widget.setStyleSheet("""

                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget { font-weight: normal; }

            """)

            # Change viewport display color to light grey
            cycle_background_color_to_light_grey()
