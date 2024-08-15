# Maya-UI-Changer

This is a suite of tools created in order to allow greater customization of Maya’s user environment. This project is currently a work in progress as such aspects of the tools may not function correctly.

Adds a new “Themes” menu item to Maya’s menu bar. Navigate to it to cycle through the available theme presets. <br>
![image](https://github.com/Aldanoah/Maya-UI-Changer/assets/84312447/e5a685f6-6293-4759-b25f-1fd127aae5f7)

Installation:
<br>
1) Download the latest "MayaUIChanger.zip"  version from the releases tab.
2) Unzip the file into your Maya 2024 script directory e.g "..\Documents\maya\2024\scripts\MayaUIChanger".
3) Copy the "userSetup.py" script to your maya script directory e.g "..\Documents\maya\2024\scripts.
5) Launch Maya.
6) if the "Themes" menu item is missing, you may alternatively run the "UIPresetLoader.py" script through Maya's script editor.

**Note:** 
You may need to set your maya script directory as a new system variable. You can do so by searching for "environment variables" on windows then performing the following steps.
![Steps](https://github.com/user-attachments/assets/c895be72-7c8e-4c20-97bd-ce2594bda4bf)

**Optional:** You may navigate to the fonts folder in the script directory to install the optional “dejavu-sans” and “Rajdhani” font packs. These fonts enhance the look of the theme presets but are not required for their functioning.

**Compatability:** **Maya 2024**.

**The currently available presets and tools are as follows;**

1) Blender Dark Preset

![Blender Dark](https://github.com/Aldanoah/Maya-UI-Changer/assets/84312447/9963682d-ed75-477b-a7ad-bb5f2a7daeab)

2) Blender Light Preset
   
![Blender Light](https://github.com/Aldanoah/Maya-UI-Changer/assets/84312447/7f2cd810-3259-4cfd-98e5-0e561c65cb0f)

3) Edgerunners Preset

![Edgerunners](https://github.com/Aldanoah/Maya-UI-Changer/assets/84312447/3dda7720-369b-470b-9921-0776e55e6add)

4) A Custom splash screen picker is bundled in this package. Run the "SplashLoader.py" to use, requires launching Maya as an Adminstrator.
![Custom Splash Picker](https://github.com/Aldanoah/MayaUIChanger/assets/84312447/44bb8352-199c-4752-8388-eb465b46409f)

5) Also bundled is a script that plays a set .wav file upon launching Maya. To use, you can set the path to your desired sound file through the "sound_file_path" variable in the included "startupSound.py" script. A user interface to simplify the process will be added at a later time. Unmute the video below to sample the script in question.


https://github.com/user-attachments/assets/b72cb5e5-51d9-4a84-8916-42b55102201a





