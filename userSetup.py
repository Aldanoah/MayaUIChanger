# Make sure that PYTHONPATH environment variable is set to your C:/user/userName/Documents/maya/scripts directory
import maya.utils
import maya.cmds as cmds

# Load UI Preset Loader Script on startup
def loadUIPresetLoader():
    import MayaUIChanger.UIPresetLoader as UIPresetLoader
    UIPresetLoader.run()  

def loadstartupsound():
    import MayaUIChanger.startupSound as startupSound

    print("test")
    try:
        # Play the custom sound file
        startupSound.run()
    except Exception as e:
        print(f"Error playing sound: {e}")

maya.utils.executeDeferred(loadUIPresetLoader)
maya.utils.executeDeferred(loadstartupsound)
