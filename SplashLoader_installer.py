import os
import maya.cmds as cmds
import maya.utils

# ---------------- CONFIG ----------------
SHELF_ANNOTATION = "SplashLoader"
MODULE_NAME = "SplashLoader"
SUBFOLDER = "MayaUIChanger"
ICON_NAME = "splash_icon.png"

# ---------------- PATH HELPERS ----------------
def get_tool_dir():
    scripts_dir = cmds.internalVar(userScriptDir=True)
    return os.path.normpath(os.path.join(scripts_dir, SUBFOLDER))

def get_script_path():
    return os.path.join(get_tool_dir(), MODULE_NAME + ".py")

def get_icon_path():
    icon_path = os.path.join(get_tool_dir(), ICON_NAME)
    return os.path.normpath(icon_path)

# ---------------- VALIDATION ----------------
def validate_files(script_path, icon_path):
    if not os.path.isfile(script_path):
        raise RuntimeError("Missing script:\n" + script_path)

    if not os.path.isfile(icon_path):
        raise RuntimeError(
            "Missing icon file:\n" + icon_path +
            "\n\nEnsure:\n"
            "- File name is exactly splash_icon.png\n"
            "- It is inside MayaUIChanger folder\n"
        )

# ---------------- SHELF INSTALL ----------------
def install_shelf():
    script_path = get_script_path()
    icon_path = get_icon_path()

    validate_files(script_path, icon_path)

    current_shelf = cmds.tabLayout("ShelfLayout", q=True, selectTab=True)
    buttons = cmds.shelfLayout(current_shelf, q=True, childArray=True) or []

    # Remove duplicates
    for b in buttons:
        if cmds.shelfButton(b, q=True, annotation=True) == SHELF_ANNOTATION:
            cmds.deleteUI(b)
    command = f'''
import importlib.util

path = r"{script_path}"

spec = importlib.util.spec_from_file_location("SplashLoader_runtime", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

mod.run()
'''

    cmds.shelfButton(
        parent=current_shelf,
        label="Splash",
        annotation=SHELF_ANNOTATION,
        command=command,
        image=str(icon_path),
        style="iconOnly"
    )

    cmds.inViewMessage(
        amg="Splash Tool Installed",
        pos='topCenter',
        fade=True
    )

# ---------------- RUN ----------------
maya.utils.executeDeferred(install_shelf)