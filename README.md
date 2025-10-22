# What's New

Updated Splash Loader 
-
• Overhauled the User Interface of the splash loader tool.

• Added a toggle that disables any prior start up sounds.

• Added automatic detection of Maya's splash image path. Though this assumes a default Maya root Installation path of "C:\Program Files\Autodesk". You will have to adjust the path in line 41 of the splashloader script if your Maya installation is in a non-standard install path. <br>

Please unmute the video preview. 

https://github.com/user-attachments/assets/da9aca25-9b0a-4e3e-b386-c3b604acc122



---

# Maya-UI-Changer

This is a suite of tools created in order to allow greater customization of Maya’s user environment. This project is currently a work in progress so some aspects may not function as intended.

Adds a new “Themes” menu item to Maya’s menu bar. Navigate to it to cycle through the available presets. <br>
<img width="424" height="277" alt="image" src="https://github.com/user-attachments/assets/7aac6bab-58fd-45b5-803b-f8de55cb2745" />




Installation:
-
1) Go to <a href="https://github.com/Aldanoah/MayaUIChanger/releases">releases</a> to download the latest "MayaUIChanger.zip" version.
2) Place the "MayaUIChanger" folder in your Maya scripts directory e.g "..\Documents\maya\2024\scripts\MayaUIChanger".
3) Copy the "userSetup.py" file in the folder to your Maya scripts directory e.g "..\Documents\maya\2024\scripts.
5) Launch Maya.
6) if the "Themes" menu item is missing, you may alternatively run the "UIPresetLoader.py" script through Maya's script editor.

Note:
-
You may need to set your Maya script directory as a new system variable. You can do so by searching for "environment variables" on windows then performing the following steps. This change is mainly required by the Splashloader script, the UI preset loader will work regardless.  
<br>
![Steps](https://github.com/user-attachments/assets/c895be72-7c8e-4c20-97bd-ce2594bda4bf)

- Navigate to the fonts folder in the script directory to install the optional “dejavu-sans” and “Rajdhani” font packs. These fonts enhance the look of the theme presets but are not required for their functioning.


**The currently available features are as follows;**
1) Apple Pro Preset by jmaruska
![Apple Pro](https://github.com/user-attachments/assets/9364a490-6cd1-4edf-aa30-c0655be27499)
   
2) Blender Dark Preset
![Blender Dark](https://github.com/user-attachments/assets/0a87f7bc-f54a-4e8f-bdf5-85bb325b88ab)

3) Blender Light Preset
![Blender Light](https://github.com/user-attachments/assets/1fa5800a-a6ad-4d83-addd-41a2aefceacb)

4) Edgerunners Preset
![Edgerunners](https://github.com/user-attachments/assets/99360561-6247-4312-a093-06eb05f2bc1f)

5) ZBrush Preset
![ZBrush](https://github.com/user-attachments/assets/d2827ec7-bf2d-48cc-aff8-197a0bf62dac)

6) Unreal Engine Preset
![UE5](https://github.com/user-attachments/assets/d80dabb1-5afa-4f05-b3a6-5b1c70aeb3ba)

7) Easy Blue Preset by 3Dsmash
![Easy Blue Preview](https://github.com/user-attachments/assets/90adef32-a333-4ea2-9314-d437b1de13fc)

8) Modo Dark Preset
![Modo Preview](https://github.com/user-attachments/assets/4eb9049d-4f9d-4c2f-9b8c-83bd27f4e2df)

9) Umbra Dark Preset
![Umbra Theme](https://github.com/user-attachments/assets/26345e52-c3d6-4405-9858-531236a84282)

10) Maya Light 2010 (Depreciated)
![Maya Light](https://github.com/user-attachments/assets/cd3c98b6-0872-4abc-a1c2-cf9e12eb0ba0)


Extras:
-

10) Maya Splash Tool 

[https://github.com/user-attachments/assets/a6a9fb27-69b7-4040-8812-99bc853d11a2](https://github.com/user-attachments/assets/da9aca25-9b0a-4e3e-b386-c3b604acc122)

A Script to customize Maya's Splash screen is also bundled with this project. It requires launching Maya with adminstrator access in order to function correctly. <br><br> The script currently only takes .wav and .png files and doesn't support resizing images so a target image size of 860x500px is recommended. Simply run the SplashLoader.py script to use. You can also save the script to your shelf for easy access. <br><br> Please unmute the video preview. 


Compatibility:
-
Maya 2024 - 2026 but likely to work on earlier versions.

Questions?
-
<a href="https://linktr.ee/Aldanoah">Contact</a>




