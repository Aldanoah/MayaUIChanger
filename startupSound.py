import winsound

def play_custom_sound(sound_file):
    try:
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Specify the path to your custom sound file
sound_file_path = r'C:\Users\chine\OneDrive\Documents\Splash\2099.wav'
play_custom_sound(sound_file_path)
