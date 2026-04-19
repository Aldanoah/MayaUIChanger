import maya.utils

# Function to Load UIPresetLoader script on startup
def loadUIPresetLoader():
    import MayaUIChanger.UIPresetLoader as UIPresetLoader
    UIPresetLoader.run()  

# Function to Load Splash script on startup
def playStartupSound():
    try:
        import MayaUIChanger.SplashLoader as Splashloader
        settings = Splashloader.load_settings()

        # Check if an audio file is set in the settings and play it
        if 'audio_file' in settings:
            Splashloader.play_startup_sound_once()
        else:
            print("No audio file found in settings.")
    except Exception as e:
        print(f"Error playing startup sound: {e}")

maya.utils.executeDeferred(loadUIPresetLoader)
maya.utils.executeDeferred(playStartupSound)
