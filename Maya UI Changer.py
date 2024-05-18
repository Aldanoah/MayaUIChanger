import maya.cmds as cmds
import shiboken2
from maya import OpenMayaUI
from PySide2 import QtWidgets

def apply_stylesheet_recursive(widget, selected_object):

    # Apply stylesheet to current widget
    if isinstance(widget, QtWidgets.QWidget):
        if selected_object == "2077":
            widget.setStyleSheet("""
                QWidget {
                    background-color: rgb(30,30,50);
                    selection-color: rgb(94,246,255); 
                    selection-background-color: rgb(247,80,70);
                    color: rgb(94,246,255);
                    font-family: rajdhani;
                    font-weight: bold;
                    font-size: 13px;
                }
                QAbstractSpinBox {
                    color: rgb(0,0,0);
                }
                QComboBox:hover,QPushButton:hover {
                    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f75049, stop: 1 #f75049);
                }  
                QTabWidget {
                    border-style: solid;
                    padding: 30px;
                    background-color: rgb(0,0,0);
                    margin: 10px;
                }
                QMainWindow::separator:hover {
                    background: red;
                }
                QTabBar::tab:selected {
                    border-style: outset;
                    border-width: 2px;
                    border-color: rgb(241, 181, 55);
                    color: rgb(241, 181, 55);
                    background-color: rgb(0,0,0);                
                }
                QScrollBar {
                    color: rgb(255,255,255); 
                    background-color: rgb(247,80,73);        
                }
                QSlider {
                    background-color: rgb(247,80,73);        
                }
                QSlider::handle {
                    background-color: rgb(94,246,255);        
                }
                QCheckBox::indicator:unchecked {
                    color: rgb(27,80,73);        
                }
                QComboBox {
                    color: rgb(29, 237, 131);
                    background-color: rgb(0,0,0);
                }
                QTabWidget::pane {
                    background-color: rgb(6,31,43);
                }
                QTextEdit {
                    color: rgb(255, 255, 255);
                    background-color: rgb(0,0,0);
                }
            """)
        elif selected_object == "Blender Dark":
            widget.setStyleSheet("""
                /*-----QWidget-----*/ 
                QWidget 
                {
                    background-color: rgb(48,48,48);
                    selection-color: rgb(254,254,254); 
                    selection-background-color: rgb(71,114,179);
                    color: rgb(215,215,215);
                    font-family: DejaVuSans;
                    font-size: 12px;
                }

                /*-----QComboBox-----*/                              
                QComboBox 
                {
                    border: 0.5px;
                    border-color: rgb(61,61,61);
                    background-color: rgb(40,40,40);
                    border-style:outset;
                    border-radius: 0.2em;
                    padding-left: 1px;           
                    min-width: 7em;
                }
                            
                /*-----QTabWidget-----*/                        
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(24,24,24);
                }

                /*-----QMenuBar-----*/             
                QMenuBar
                {
                    background-color: rgb(24,24,24);
                    border: 1px;
                }
                                 
                QMenuBar::item 
                {
	                background-color: transparent;
                }
                                 
                QMenuBar::item:selected 
                {
                    background-color: rgb(63,63,63);
                    border-style:outset;
                    border-radius: 0.2em; 
                }
                            
                /*-----QTabBar-----*/
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
                    background-color: rgb(48,48,48);              
                }
                                 
                QTabBar::tab:!selected 
                {
                    color: rgb(147,147,147); 
                    background-color: rgb(29,29,29);            
                }
                                 
                QTabBar::tab:!selected:hover
                {
	                border-top-color: rgb(155,155,155);
                }
                                 
                QTabBar::tab:last
                {
                    border-top-right-radius: 0em;
	                margin-right: 0; 
                }
                
                /*-----QTextEdit-----*/ 
                QTextEdit 
                {
                    color: rgb(149, 214, 000);
                    background-color: rgb(0,0,0);
                }

                /*-----QScrollBar-----*/               
                QScrollBar
                {
                    color: rgb(36,36,36); 
                    background-color: rgb(84,84,84);        
                }

                /*-----QSlider-----*/                  
                QSlider 
                {
                    background-color: rgb(84,84,84);        
                }
                                 
                QSlider::handle 
                {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #fff, stop:1 #ddd);
                    border: 1px solid #444;
                    border-radius: 4px; 
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
                
                /*-----QCheckBox-----*/
                
                QCheckBox
                {
	                background-color: transparent;
                }
                QCheckBox::indicator:unchecked 
                {
                    background-color: rgb(84,84,84);
                    border-radius: 0.2em;  
                }    
                                 
                QCheckBox::indicator:checked
                {
                    image: url('D:/Maya/Scripts/Images/checkmark-16.ico');
                    width: 12px;
                    height: 12px;
                    background-color: rgb(71,114,179);
                    border-radius: 0.2em;  
                }   

                /*-----QLineEdit-----*/                 
                QLineEdit
                {
                    border: 0.5px;
                    border-color: rgb(61,61,61);
                    border-style:outset;
                    border-radius: 0.2em;
                    padding: 3px;
                    background-color: rgb(40,40,40);
                    selection-background-color: darkgray;
                }

                /*-----QLabel-----*/                  
                QLabel 
                {
	                background-color: solid;
                }
                    
                /*-----QGroupBox-----*/
                QGroupBox 
                {
                    border: 1px solid;
                    border-color: #666666;
	                border-radius: 5px;
                    background-color: rgb(61,61,61);
                    margin-top: 20px;
                }
                                 
                QGroupBox::title  
                {
                    background-color: transparent;
                    subcontrol-origin: margin;
                }
            """)

def change_interface_color(selected_object):

    # Get main Maya window
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        main_window = shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        apply_stylesheet_recursive(main_window, selected_object)
    else:
        print("Failed to find main Maya window.")

def on_theme_change(*args):
    selected_object = cmds.optionMenuGrp(UI_DropDown, q=True, v=True)
    change_interface_color(selected_object)

winName = "Blendify"
if cmds.window(winName, q=True, ex=True):
    cmds.deleteUI(winName)
cmds.window(winName)

column_layout = cmds.columnLayout(adjustableColumn=True, columnAttach=['both', 10], rowSpacing=10)

cmds.separator(height=10)
cmds.text(label="I can't believe its not Blender")
cmds.separator(height=10)

UI_DropDown = cmds.optionMenuGrp(l="Select Theme", cc=on_theme_change, en=True)
cmds.menuItem(l="Please make your selection from the list below")
cmds.menuItem(l="2077")
cmds.menuItem(l="Blender Dark")

Splash = cmds.image(image='D:\Maya\Scripts\Images\heroimage.png', vis=True)

cmds.setParent('..')
cmds.showWindow()
