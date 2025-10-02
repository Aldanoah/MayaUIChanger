# What's New

This fork adds a few improvements to the Theme Loader script:
-
• Custom QSS Tokens: Introduced myQWidget and myQMenu tokens to isolate styling to application menus (QmayaMenuBar) while leaving marking menus opaque. This prevents unwanted transparency in marking menus and ensures consistent background styling.

• Targeted Repainting: Added automatic clearing and repainting of paint-driven widgets (e.g., color sliders, swatches) to maintain proper visual updates without overriding custom themes. This is still a bit in development - but generally it works. Attribute Editor color swatches render fairly automatically, panels like the Multi-lister editor, or the Color Preferences panel will correctly render after a value change - I'm looking for ways to spoof a value change on panel load to get the swatches to automaticaly refresh.

• Event Filters: Applied filters to top-level windows and menus to dynamically enforce styling when widgets are shown, minimizing manual intervention. These event listeners are what make the above possible since they can dynamically inject theme data at run-time.

• Added my own Apple Pro theme that is inspired by Motion and Final Cut Pro. This theme leverages the custom tokens and used a Qt element inspector to target some specific elements. <br>

![Apple Pro Theme](https://raw.githubusercontent.com/jmaruska/MayaUIChanger/refs/heads/main/applepro_theme.png)


---

# Maya-UI-Changer

This is a suite of tools created in order to allow greater customization of Maya’s user environment. This project is currently a work in progress so some aspects may not function as intended.

Adds a new “Themes” menu item to Maya’s menu bar. Navigate to it to cycle through the available presets. <br>
![menu](https://github.com/user-attachments/assets/73f35de8-b935-41e9-bb7a-c19391136cce)




Installation:
-
1) Go to <a href="https://github.com/Aldanoah/MayaUIChanger/releases">releases</a> to download the latest "MayaUIChanger.zip" version.
2) Place the "MayaUIChanger" folder in your Maya scripts directory e.g "..\Documents\maya\2024\scripts\MayaUIChanger".
3) Copy the "userSetup.py" file in the folder to your Maya scripts directory e.g "..\Documents\maya\2024\scripts.
5) Launch Maya.
6) if the "Themes" menu item is missing, you may alternatively run the "UIPresetLoader.py" script through Maya's script editor.

Note:
-
You may need to set your maya script directory as a new system variable. You can do so by searching for "environment variables" on windows then performing the following steps.
<br>
![Steps](https://github.com/user-attachments/assets/c895be72-7c8e-4c20-97bd-ce2594bda4bf)

- Navigate to the fonts folder in the script directory to install the optional “dejavu-sans” and “Rajdhani” font packs. These fonts enhance the look of the theme presets but are not required for their functioning.


**The currently available features are as follows;**

1) Blender Dark Preset
![Blender Dark](https://github.com/user-attachments/assets/0a87f7bc-f54a-4e8f-bdf5-85bb325b88ab)

2) Blender Light Preset
![Blender Light](https://github.com/user-attachments/assets/1fa5800a-a6ad-4d83-addd-41a2aefceacb)

3) Edgerunners Preset
![Edgerunners](https://github.com/user-attachments/assets/99360561-6247-4312-a093-06eb05f2bc1f)

4) ZBrush Preset
![ZBrush](https://github.com/user-attachments/assets/d2827ec7-bf2d-48cc-aff8-197a0bf62dac)

5) Unreal Engine Preset
![UE5](https://github.com/user-attachments/assets/d80dabb1-5afa-4f05-b3a6-5b1c70aeb3ba)

6) Easy Blue Preset by 3Dsmash
![Easy Blue Preview](https://github.com/user-attachments/assets/90adef32-a333-4ea2-9314-d437b1de13fc)

7) Modo Dark Preset
![Modo Preview](https://github.com/user-attachments/assets/4eb9049d-4f9d-4c2f-9b8c-83bd27f4e2df)

8) Umbra Dark Preset
![Umbra Theme](https://github.com/user-attachments/assets/26345e52-c3d6-4405-9858-531236a84282)

9) Maya Light 2010 (Depreciated)
![Maya Light](https://github.com/user-attachments/assets/cd3c98b6-0872-4abc-a1c2-cf9e12eb0ba0)


Extras:
-

10) Maya Splash Tool 

https://github.com/user-attachments/assets/a6a9fb27-69b7-4040-8812-99bc853d11a2

A Script to customize Maya's Splash screen is also bundled with this project. It requires launching Maya as an adminstrator in order to function correctly. The script currently only takes .wav and .png files and doesn't support resizing images so a target image size of 860x500px is recommended. Simply run the SplashLoader.py script to use. <br><br> Please unmute the video preview. 


Compatibility:
-
Maya 2024 - 2026 but likely to work on earlier versions.

Questions?
-
<a href="https://linktr.ee/Aldanoah">Contact</a>




