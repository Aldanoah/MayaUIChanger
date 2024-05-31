import maya.cmds as cmds
import shiboken2
from maya import OpenMayaUI
from PySide2 import QtWidgets

#Start of Functions
def on_theme_change(*args):
    selected_object = cmds.optionMenuGrp(UI_DropDown, q=True, v=True)
    change_interface_color(selected_object)

def change_interface_color(selected_object):

    # Get main Maya window
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        main_window = shiboken2.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        apply_stylesheet_recursive(main_window, selected_object)
    else:
        print("Failed to find main Maya window.")
     
def apply_stylesheet_recursive(widget, selected_object):

    # Apply stylesheet to current widget
    if isinstance(widget, QtWidgets.QWidget):
        if selected_object == "2077":
            widget.setStyleSheet("""
            /*-----QWidget-----*/ 
                QWidget {
                    background-color: rgb(30,30,50);
                    selection-color: rgb(94,246,255); 
                    selection-background-color: rgb(247,80,70);
                    color: rgb(94,246,255);
                    font-family: rajdhani;
                    font-weight: bold;
                    font-size: 13px;
                }
                QComboBox:hover,QPushButton:hover {
                    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0W, y2: 1, stop: 0 #f75049, stop: 1 #f75049);
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
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget 
                {
                    background-color: rgb(48,48,48);
                    selection-color: rgb(254,254,254);
                    selection-background-color: rgb(71,114,179);
                    color: rgb(215,215,215);
                    font-family: DejaVuSans;
                    font-size: 12px;
                }

                /*-----QComboBox------------------------------------------------------------------------------------------------------------------------------------*/                          
                QComboBox 
                {
                    background-color: rgb(40,40,40);
                    border-radius: 0.2em;
                    padding-left: 6px;           
                    min-width: 7em;
                }
                
                QComboBox:on
                {
                    background-color: rgb(67,97,143);
                }
                                 
                QComboBox QAbstractItemView
                {
                selection-background-color: rgb(63,63,63);
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
                    border-radius: 0.2em;
                    width: 15px;
                    border-left-width: 0px;    
                }
                            
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/                        
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(24,24,24);
                }

                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar
                {
                    background-color: rgb(24,24,24);
                    border: 1px;
                }
                        
                QMenu::item
                {
                    border-radius: 0.5em;
                    background-color: transparent;
                    padding: 2px 20px 2px 20px; 
                }
                                 
                QMenuBar::item 
                {
                    color: rgb(193,193,193);
	                background-color: transparent;
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(225,225,225);
                    background-color: rgb(63,63,63);
                    border-style:outset;
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
                    border-top-right-radius: 0.3em;
	                margin-right: 0; 
                }
                
                /*-----QTextEdit------------------------------------------------------------------------------------------------------------------------------------*/ 
                QTextEdit 
                {
                    color: rgb(149, 214, 000);
                    background-color: rgb(0,0,0);
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
                    background-color: rgb(24,24,24);
                    border: 1px solid #404040;
                    border-color: rgb(61,61,61);
                    border-style:outset;
                    border-radius: 0.3em;
                    padding: 2px;
                    background-color: #2c2c2c;
                    selection-background-color: darkgray;
                }

                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    background-color: transparent;
                    color:#e6e6e6;
                }
                    
                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QGroupBox 
                {
                    border: 0px solid #373737;
                    background-color: #373737;
                    padding-top: 12px;
                    border-color: #666666;
	                border-radius: 5px;
                    margin-top: 20px;
                }
                                 
                QGroupBox::title  
                {
                    background-color: transparent;
                    subcontrol-origin: margin;
                    margin-top: 4px;
                    padding-left: 8px;
                }

                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QHeaderView
                {
                    background-color: #3b3b3b;
                    border: 0px transparent transparent;
                }

                QHeaderView:section {
                    background-color: #3b3b3b;
                    border: 0px transparent transparent;
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

                QMessageBox QPushButton 
                {
                    min-width: 10px;
                }

            """)
        elif selected_object == "Blender Light":
            widget.setStyleSheet("""
                /*-----QWidget------------------------------------------------------------------------------------------------------------------------------------*/ 
                QWidget 
                {
                    background-color: rgb(179,179,179);
                    selection-color: rgb(254,254,254);
                    selection-background-color: rgb(86,128,194);
                    color: rgb(40,40,40);
                    font-family: DejaVuSans;
                    font-size: 12px;
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
                    background-color: rgb(118,118,118);
                }
                                 
                QComboBox QAbstractItemView
                {
                selection-background-color: rgb(5,5,5);
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
                    border-radius: 0.2em;
                    width: 15px;
                    border-left-width: 0px;    
                }
                            
                /*-----QTabWidget------------------------------------------------------------------------------------------------------------------------------------*/                        
                QTabWidget::pane 
                {
                    top: 1px;
                    background-color: rgb(179,179,179);
                }

                /*-----QMenu------------------------------------------------------------------------------------------------------------------------------------*/           
                QMenuBar
                {
                    background-color: rgb(179,179,179);
                    border: 1px;
                }
                        
                QMenu::item
                {
                    border-radius: 0.5em;
                    background-color: transparent;
                    padding: 2px 20px 2px 20px; 
                }
                                 
                QMenuBar::item 
                {
                    color: rgb(37,37,37);
	                background-color: transparent;
                }
                                 
                QMenuBar::item:selected 
                {
                    color: rgb(225,225,225);
                    background-color: rgb(94,132,191);
                    border-style:outset;
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
                    background-color: rgb(24,24,24);
                    border-color: rgb(61,61,61);
                    border-style:outset;
                    border-radius: 0.3em;
                    padding: 2px;
                    background-color: #2c2c2c;
                    selection-background-color: darkgray;
                }

                /*-----QLabel------------------------------------------------------------------------------------------------------------------------------------*/                
                QLabel 
                {
                    background-color: transparent;
                    color: rgb(13,13,13);
                }
                    
                /*-----QGroupBox------------------------------------------------------------------------------------------------------------------------------------*/ 
                QGroupBox 
                {
                    border: 0px solid #373737;
                    background-color: #373737;
                    padding-top: 12px;
                    border-color: #666666;
	                border-radius: 5px;
                    margin-top: 20px;
                }
                                 
                QGroupBox::title  
                {
                    background-color: transparent;
                    subcontrol-origin: margin;
                    margin-top: 4px;
                    padding-left: 8px;
                }

                /*-----QHeaderView------------------------------------------------------------------------------------------------------------------------------------*/ 
                QHeaderView
                {
                    background-color: #3b3b3b;
                    border: 0px transparent transparent;
                }

                QHeaderView:section {
                    background-color: #3b3b3b;
                    border: 0px transparent transparent;
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

                QMessageBox QPushButton 
                {
                    min-width: 10px;
                }
            """) 
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

column_layout = cmds.columnLayout(adjustableColumn=True, columnAttach=['both', 10], rowSpacing=10)
cmds.separator(height=10)
cmds.text(label="Maya UI Changer")
cmds.separator(height=10)

#Drop Down to Select Theme
UI_DropDown = cmds.optionMenuGrp(l="Select Theme", cc=on_theme_change, en=True)
cmds.menuItem(l="Please make your selection from the list below")
cmds.menuItem(l="Maya")
cmds.menuItem(l="Blender Dark")
cmds.menuItem(l="Blender Light")
cmds.menuItem(l="2077")

# Main Widget UI
QMainWidget=cmds.text(l="Main Widget",bgc=(.4,.4,.4),w=340,h=25)
QWidgetC=cmds.colorIndexSliderGrp( label='Color: ', min=0, max=20, value=8)
QWidgetBGC=cmds.colorIndexSliderGrp( label='Background Color: ', min=0, max=20, value=2)
QWidgetSC=cmds.colorIndexSliderGrp( label='Selection Color: ', min=0, max=20, value=4)
QWidgetSBGC=cmds.colorIndexSliderGrp( label='Selection BG Color: ', min=0, max=20, value=6)

cmds.setParent('..')
cmds.showWindow()