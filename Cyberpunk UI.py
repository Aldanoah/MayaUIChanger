import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from maya import OpenMayaUI
from PySide2 import QtWidgets, QtCore

#Start of Functions
def on_theme_change(theme):
    change_interface_color(theme)

def change_interface_color(selected_object):
    # Get main Maya window
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
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

    # Apply stylesheet to current widget
    if isinstance(widget, QtWidgets.QWidget):
        if selected_object == "Edgerunners":
            widget.setStyleSheet("""
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget
                {
                    background-color: rgb(30,30,50);
                    color: rgb(94,246,255);
                    selection-color: rgb(94,246,255); 
                    selection-background-color: rgb(247,80,70);
                    font-family: rajdhani;
                    font-weight: bold;
                    font-size: 13px;
                }
                          
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTableView, QTreeView
                {
                background-color: rgb(48,48,48);
                }   
                                 
                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/
                QComboBox {
                    color: rgb(29, 237, 131);
                    background-color: rgb(0,0,0);
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                                 
                QComboBox:on
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                }
                
                QComboBox:disabled 
                {
                    background-color: rgb(14,11,18);
                    color: rgb(123,39,39);
                }
                                 
                QComboBox:hover,QPushButton:hover 
                {
                    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0W, y2: 1, stop: 0 #f75049, stop: 1 #f75049);
                }
                                   
                QComboBox::down-arrow
                {
                    image: url('D:/Maya/Scripts/Images/Arrow-204-16.ico');
                    width: 8px;
                    height: 8px;
                }
                
                QComboBox::drop-down
                {
                    width: 15px;
                    border-radius: 0.2em;
                    border-left-width: 0px;    
                }
                
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/            
                QMenu
                {
                    background-color: transparent;
                }
                                 
                QMenu::item
                {
                    background-color: transparent;
                }
                
                QMenu::separator
                {
                    height:0px;
                    margin-left:5px;
                    margin-right:5px;
                }

                QMenuBar
                {
                    background-color: transparent;
                    spacing:2px;
                    border: 1px;
                }
                                 
                QMenuBar::item 
                {
	                background-color: transparent;
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                    border-style: outset;
                    border-radius: 0.2em; 
                }
                                 
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/                       
                QTabBar::tab
                {
	                border-width: 1px;
	                padding: 5px;
	                padding-left: 10px;
	                padding-right: 10px;
                    border-top-left-radius: 0.3em;
                    border-top-right-radius: 0.3em;
                    border-bottom-style: solid; 
                }  
                
                QTabBar::tab:selected {
                    border-style: solid;
                    color: rgb(94,246,255);
                    background-color: rgb(14,11,18);   
                }
                
                QTabBar::tab:!selected 
                {
                    color: rgb(29,237,131);
                    background-color: rgb(14,11,18);          
                } 

                QTabBar::tab:hover:!selected 
                {
                    color: rgb(94,246,255);
                    background-color: rgb(123,39,39);
                }  

                QTabBar::tab:last
                {
                    border-top-right-radius: 0em;
	                margin-right: 0; 
                }   

                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/
                QTabWidget::pane 
                {
                    background-color: rgb(14,11,18);
                } 
                
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/
                QTextEdit 
                {
                    color: rgb(255,255,255);
                    background-color: rgb(14,11,18);
                }
                                 
                QTextEdit:!editable 
                {
                    background-color: rgb(14,11,18);
                }

                /*-----QScrollBar-----------------------------------------------------------------------------------------------------------------------------------*/               
                QScrollBar 
                {
                    color: rgb(255,255,255); 
                    background-color: rgb(247,80,73);        
                }
                
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical 
                {
                    background-color: rgb(14,11,18);      
                }
                
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal 
                {
                    background-color: rgb(14,11,18); 
                }
                                 
                /*-----QSlider-----------------------------------------------------------------------------------------------------------------------------------*/
                QSlider 
                {
                    background-color: rgb(247,80,73);        
                }
                                 
                QSlider::handle 
                {
                    background-color: rgb(94,246,255);        
                }
                
                QSlider::add-page:horizontal:disabled 
                {
                    background-color: rgb(123,39,39);
                }
                
                QSlider::sub-page:horizontal:disabled 
                {
                    background-color: rgb(247,80,73); 
                }
                                 
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/                
                QCheckBox
                {
	                background-color: transparent;
                }
                                 
                QCheckBox::indicator 
                {
                    width: 12px;
                    height: 12px;
                }

                QCheckBox::indicator:checked
                {
                    image: url('D:/Maya/Scripts/Images/checkmark-16.ico');
                    background-color: rgb(247,80,70);
                    border-radius: 0.2em;  
                } 
                                             
                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(14,11,18);
                    border-radius: 0.2em;  
                }   
                    
                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/
                QLineEdit
                {
                    color: rgb(29, 237, 131);
                    background-color: rgb(14,11,18);
                    border-color: rgb(61,61,61);
                    border-radius: 0.3em;
                    padding: 0px;
                }
                                 
                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    color: rgb(94,246,255);
                    background-color: transparent;
                }
                
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/ 
                QProgressBar 
                {
                    background-color: #424242;
                    border: 1px solid #373737;
                    padding: 0px;
                    text-align: right;
                }
                                 
                QProgressBar::chunk {
                    background-color: #5680c2;
                    border: 1px solid #373737;
                }
                                 
            """)

            # cycle the background color to black
            cycle_background_color_to_black()

        elif selected_object == "Blender Dark":
            widget.setStyleSheet("""
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget 
                {
                    background-color: rgb(48,48,48);
                    color: rgb(216,216,216);
                    selection-color: rgb(254,254,254);
                    selection-background-color: rgb(86,128,194);
                    font-family: DejaVuSans;
                    font-size: 12px;
                }
                                 
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTableView, QTreeView
                {
                background-color: rgb(48,48,48);
                }   

                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox 
                {
                    color: rgb(216,216,216);
                    background-color: rgb(29,29,29); 
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                
                QComboBox:on
                {
                    background-color: rgb(67,97,143);
                }
                                 
                QComboBox:disabled 
                {
                    background-color: #323232;
                    color: #8a8a8a;
                }

                QComboBox::down-arrow
                {
                    image: url('D:/Maya/Scripts/Images/Arrow-204-16.ico');
                    width: 8px;
                    height: 8px;
                }
                                 
                QComboBox::drop-down
                {
                    width: 15px;
                    border-radius: 0.2em;
                    border-left-width: 0px;    
                }
                            
                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenu
                {
                    background-color: rgb(82,82,82);
                }
                                 
                QMenu::item
                {
                    background-color: transparent;
                }

                QMenu::separator
                {
                    height:0px;
                    margin-left:5px;
                    margin-right:5px;
                }

                QMenuBar
                {
                    background-color: transparent;
                    spacing:2px;
                    border: 1px;
                }
                                 
                QMenuBar::item 
                {
                    color: rgb(193,193,193);
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(225,225,225);
                    background-color: rgb(94,132,191);
                    border-style: outset;
                    border-radius: 0.2em; 
                }
                          
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTabBar::tab
                {
	                border-width: 1px;
	                border-bottom: none;
	                padding: 5px;
	                padding-left: 10px;
	                padding-right: 10px;
                    border-top-left-radius: 0.3em;
                    border-top-right-radius: 0.3em;
                    border-bottom-style: solid; 
                }    
                                   
                QTabBar::tab:selected 
                {
                    background-color: #424242;
                    border-style: solid;
                    border-width: 1px;
                    border-color: #373737;
                    border-bottom-color: #424242;            
                }

                QTabBar::tab:!selected 
                {
                    color: #afafaf;
                    background-color: rgb(29,29,29);            
                }

                QTabBar::tab:hover:!selected 
                {
                    background-color: #343434;
                    color: #afafaf;
                }
                                 
                QTabBar::tab:last
                {
                    border-top-right-radius: 0em;
	                margin-right: 0; 
                }
                
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/                        
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(29,29,29); 
                }

                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTextEdit 
                {
                    color: rgb(149, 214, 000);
                    background-color: rgb(29,29,29);
                }
                
                QTextEdit:!editable 
                {
                    background-color: rgb(29,29,29);
                }

                /*-----QScrollBar------------------------------------------------------------------------------------------------------------------------------------*/             
                QScrollBar
                {
                    margin: 0px;
                    padding: 0px;   
                }
                
                QScrollBar:vertical 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    width: 13px;
                }
                                 
                QScrollBar:horizontal 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    height: 13px;
                }
                                 
                QScrollBar::handle:vertical {
                    background-color: #545454;
                    border-radius: 4px;

                }
                QScrollBar::handle:horizontal {
                    background-color: #545454;
                    border-radius: 4px;
                }

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background-color: rgb(36,36,36);
                }

                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background-color: rgb(36,36,36);
                }

                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/                
                QSlider 
                {
                    background-color: rgb(84,84,84);        
                }
                                 
                QSlider::handle 
                {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #fff, stop:1 #ddd);
                    border: 1px solid #444;
                }
                            
                QSlider::sub-page:horizontal 
                {
                    background: rgb(71,114,179);
                }
                                 
                QSlider::handle:horizontal:hover
                {
                    background: rgb(71,114,179);
                    border-radius: 0px;
                }
                                 
                QSlider::add-page:horizontal:disabled 
                {
                    background: rgb(40,40,40);
                    border-color: #999;
                }
                                 
                QSlider::handle:horizontal:disabled 
                {
                    background: #eee;
                    border: 1px solid #aaa;
                    border-radius: 4px;
                }
                
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QCheckBox
                {
	                background-color: transparent;
                }

                QCheckBox::indicator 
                {
                    width: 12px;
                    height: 12px;
                }
                           
                QCheckBox::indicator:checked
                {
                    image: url('D:/Maya/Scripts/Images/checkmark-16.ico');
                    background-color: rgb(71,114,179);
                    border-radius: 0.2em;  
                }  

                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(84,84,84);
                    border-radius: 0.2em;  
                }

                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/                 
                QLineEdit
                {
                    color: rgb(195,195,195);
                    background-color: rgb(29,29,29);
                    border: 1px solid #404040;
                    border-color: rgb(61,61,61);
                    border-radius: 0.3em;
                    padding: 0px;
                }

                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    color: rgb(216,216,216);
                    background-color: transparent;

                }

                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/ 
                QProgressBar 
                {
                    background-color: #424242;
                    border: 1px solid #373737;
                    padding: 0px;
                    text-align: right;
                }
                                 
                QProgressBar::chunk {
                    background-color: #5680c2;
                    border: 1px solid #373737;
                }

                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QMessageBox 
                {
                    color: rgb(40,40,40)
                    background-color: rgb(192, 192, 192);
                }
                
                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/   
                QPushButton 
                {
                    color: rgb(37,37,37);
                } 

            """)

            # cycle the viewport background color to black
            cycle_background_color_to_black()

        elif selected_object == "Blender Light":
            widget.setStyleSheet("""
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget
                {
                    background-color: rgb(192, 192, 192);
                    color: rgb(216,216,216);
                    selection-color: rgb(254,254,254);
                    selection-background-color: rgb(86,128,194);
                    font-family: DejaVuSans;
                    font-size: 12px;
                }
                                 
                /*-----QTableView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTableView, QTreeView
                {
                background-color: rgb(59,59,59);
                }   

                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox 
                {
                    color: rgb(216,216,216);
                    background-color: rgb(59,59,59);
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                
                QComboBox:on
                {
                    background-color: rgb(67,97,143);
                }
                                 
                QComboBox:disabled 
                {
                    background-color: #323232;
                    color: #8a8a8a;
                }

                QComboBox::down-arrow
                {
                    image: url('D:/Maya/Scripts/Images/Arrow-204-16.ico');
                    width: 8px;
                    height: 8px;
                }
                                 
                QComboBox::drop-down
                {
                    width: 15px;
                    border-radius: 0.2em;
                    border-left-width: 0px;    
                }

                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/                    
                QMenu
                {
                    background-color: rgb(82,82,82);
                }
                                 
                QMenu::item
                {
                    background-color: transparent;
                }

                QMenu::separator
                {
                    height:0px;
                    margin-left:5px;
                    margin-right:5px;
                }

                QMenuBar
                {
                    background-color: transparent;
                    spacing:2px;
                    border: 1px;
                }
                                 
                QMenuBar::item 
                {
                    color: rgb(37,37,37);
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(225,225,225);
                    background-color: rgb(94,132,191);
                    border-style: outset;
                    border-radius: 0.2em; 
                }
                          
                /*-----QTabBar------------------------------------------------------------------------------------------------------------------------------------*/                
                QTabBar::tab 
                {
	                border-width: 1px;
	                border-bottom: none;
	                padding: 5px;
	                padding-left: 10px;
	                padding-right: 10px;
                    border-top-left-radius: 0.3em;
                    border-top-right-radius: 0.3em;
                    border-bottom-style: solid; 
                }   
                                   
                QTabBar::tab:selected 
                {
                    color: rgb(40,40,40);
                    background-color: rgb(179,179,179);
                    border-style: solid;
                    border-width: 1px;
                    border-color: #373737;
                    border-bottom-color: #424242;            
                }

                QTabBar::tab:!selected 
                {
                    color: rgb(33,33,33);
                    background-color: rgb(139,139,139);            
                }

                QTabBar::tab:hover:!selected 
                {
                    color: rgb(33,33,33);
                    background-color: rgb(146,146,146);
                }
                                 
                QTabBar::tab:last
                {
                    border-top-right-radius: 0.3em;
	                margin-right: 0; 
                }
                
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/                                     
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(179,179,179);
                }
                                 
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTextEdit 
                {
                    color: rgb(149, 214, 000);
                    background-color: rgb(29,29,29);
                }
                
                QTextEdit:!editable 
                {
                    background-color: rgb(29,29,29);
                }

                /*-----QScrollBar------------------------------------------------------------------------------------------------------------------------------------*/             
                QScrollBar
                {
                    margin: 0px;
                    padding: 0px;   
                }
                
                QScrollBar:vertical 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    width: 13px;
                }
                                 
                QScrollBar:horizontal 
                {
                    border: 1px solid #3D3A3A;
                    background-color: none;
                    height: 13px;
                }
                                 
                QScrollBar::handle:vertical {
                    background-color: #545454;
                    border-radius: 4px;

                }
                QScrollBar::handle:horizontal {
                    background-color: #545454;
                    border-radius: 4px;
                }

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background-color: rgb(146,146,146);
                }

                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background-color: rgb(146,146,146);
                }

                /*-----QSlider------------------------------------------------------------------------------------------------------------------------------------*/                
                QSlider 
                {
                    background-color: rgb(84,84,84);        
                }
                                 
                QSlider::handle 
                {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #fff, stop:1 #ddd);
                    border: 1px solid #444;
                }
                            
                QSlider::sub-page:horizontal 
                {
                    background: rgb(71,114,179);
                }
                                 
                QSlider::handle:horizontal:hover
                {
                    background: rgb(71,114,179);
                    border-radius: 0px;
                }
                                 
                QSlider::add-page:horizontal:disabled 
                {
                    background: rgb(40,40,40);
                    border-color: #999;
                }
                                 
                QSlider::handle:horizontal:disabled 
                {
                    background: #eee;
                    border: 1px solid #aaa;
                    border-radius: 4px;
                }
                
                /*-----QCheckBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QCheckBox
                {
	                color: rgb(37,37,37);
                }

                QCheckBox::indicator 
                {
                    width: 12px;
                    height: 12px;
                }
                           
                QCheckBox::indicator:checked
                {
                    image: url('D:/Maya/Scripts/Images/checkmark-16.ico');
                    background-color: rgb(71,114,179);
                    border-radius: 0.2em;  
                }  

                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(84,84,84);
                    border-radius: 0.2em;  
                }
                                 
                /*-----QRadioButton------------------------------------------------------------------------------------------------------------------------------------*/ 
                QRadioButton
                {
	                color: rgb(37,37,37);
                }   

                /*-----QLineEdit------------------------------------------------------------------------------------------------------------------------------------*/                 
                QLineEdit
                {
                    color: rgb(195,195,195);
                    background-color: rgb(59,59,59);
                    border: 1px solid #404040;
                    border-color: rgb(61,61,61);
                    border-radius: 0.3em;
                    padding: 0px;
                }

                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    color: rgb(37,37,37);
                    background-color: transparent;
                }
                            
                /*-----QProgressBar------------------------------------------------------------------------------------------------------------------------------------*/ 
                QProgressBar 
                {
                    background-color: #424242;
                    border: 1px solid #373737;
                    padding: 0px;
                    text-align: right;
                }
                                 
                QProgressBar::chunk {
                    background-color: #5680c2;
                    border: 1px solid #373737;
                }

                /*-----QMessageBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QMessageBox 
                {
                    color: rgb(179,179,179);
                    background-color: rgb(192, 192, 192);
                } 

                /*-----QPushButton------------------------------------------------------------------------------------------------------------------------------------*/   
                QPushButton 
                {
                    color: rgb(37,37,37);
                    background-color: rgb(192, 192, 192);
                } 
               
            """) 

            # cycle the viewport background color to light grey
            cycle_background_color_to_light_grey()

        elif selected_object == "Maya":
            widget.setStyleSheet("""
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget 
                {
                    font-family: DejaVuSans;
                    font-size: 12px;
                }                                          
        """) 

#Start of UI
winName = "Maya UI Changer"
if cmds.window(winName, q=True, ex=True):
    cmds.deleteUI(winName)
cmds.window(winName)

form = cmds.formLayout()
title = cmds.text(label="Maya UI Changer", align="center", height=30)

themes = ["Blender Dark", "Blender Light", "Edgerunners", "Maya"]
icon_paths = {
    "Blender Dark": "D:/Maya/Scripts/Images/Blender_logo_1.png",
    "Blender Light": "D:/Maya/Scripts/Images/Blender_logo_2.png",  
    "Edgerunners": "D:/Maya/Scripts/Images/Edgerunners_logo_1.png",  
    "Maya": "D:/Maya/Scripts/Images/Maya_logo_1.png"  
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
