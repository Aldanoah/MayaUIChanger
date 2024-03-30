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
                    background-color: rgb(6,31,43);
                    color: rgb(241,181,55);
                    font-family: play;
                }
                QComboBox:hover,QPushButton:hover {
                    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
                }  
                QTabWidget {
                    color: rgb(255, 0, 0);
                    border-style: solid;
                    padding: 20px;
                    background-color: rgb(0,0,0);
                    margin: 10px;
                }
                QCheckBox:disabled {
                    color: rgb(214, 208, 208);
                }
                QMainWindow::separator:hover {
                    background: red;
                }
                QTabBar::tab:selected {
                    font-family: play;
                    border-style: solid;
                    color: rgb(29, 237, 131);
                    background-color: rgb(0,0,0);                
                }
                QScrollBar {
                    color: rgb(251,147,48); 
                    background-color: rgb(247,80,73);             
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
        elif selected_object == "2023":
            widget.setStyleSheet("""
                QWidget {
                    background-color: rgb(6,31,43);
                    color: rgb(0, 255, 0);
                    font-family: play;
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

winName = "Script UI Changer"
if cmds.window(winName, q=True, ex=True):
    cmds.deleteUI(winName)
cmds.window(winName)

column_layout = cmds.columnLayout(adjustableColumn=True, columnAttach=['both', 10], rowSpacing=10)

cmds.separator(height=10)
cmds.text(label="Wake Up Samurai, We have a City to Burn")
cmds.separator(height=10)

UI_DropDown = cmds.optionMenuGrp(l="Select Theme", cc=on_theme_change, en=True)
cmds.menuItem(l="Please make your selection from the list below")
cmds.menuItem(l="2077")
cmds.menuItem(l="2023")

cyberSplash = cmds.image(image='C:/Users/chine/Downloads/Cyberpunk+logo+Resource/Cyberpunk logo Resource rez.png', vis=True)

cmds.setParent('..')
cmds.showWindow()
