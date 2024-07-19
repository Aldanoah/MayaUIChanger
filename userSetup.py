# Make sure that PYTHONPATH environment variable is set to your C:/user/userName/Documents/maya/scripts directory

import maya.cmds as cmds
import maya.utils

# Load UI Preset Loader Script on startup
def loadUIPresetLoader():
    myScriptDir = cmds.internalVar(userAppDir=True) + "2024/scripts/MayaUIChanger/"
    script_path = myScriptDir + 'UIPresetLoader.py'
    exec(open(script_path).read())

maya.utils.executeDeferred(loadUIPresetLoader)
