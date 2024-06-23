import maya.cmds as cmds

def create_menu():
    # Check if the menu already exists, if so, delete it
    if cmds.menu('myMenu', exists=True):
        cmds.deleteUI('myMenu', menu=True)
    
    # Create a new menu in the main Maya window
    cmds.menu('myMenu', label='Themes', parent='MayaWindow', tearOff=True)

    # Add a submenu
    cmds.menuItem(subMenu=True, label='Blender')
    cmds.menuItem(label='Blender Dark', command='cmds.polyCone()')
    cmds.menuItem(label='Blender Light', command='cmds.polyCylinder()')
    cmds.setParent('..', menu=True)

    # Add a new menu item
    cmds.menuItem(label='Edgerunners')
    cmds.menuItem(label='Maya Default')

# function to create the menu
create_menu()
