from gtts import gTTS
from playsound import playsound
import os
import webbrowser

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def mini_jarvis():
    print("Welcome! I'm your voice assistant JARVIS.")
    speak("Welcome! I'm your voice assistant JARVIS.")

    while True:
        command = input("You: ").lower()

        if 'weather' in command:
            speak("Fetching weather information for you.")
            webbrowser.open("https://www.google.com/search?q=weather")

        elif 'youtube' in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'google' in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'exit' in command or 'bye' in command:
            speak("Goodbye! Have a great day.")
            print("JARVIS: Goodbye!")
            break

        else:
            # Smart fallback: do a Google search
            speak("Searching Google for your request.")
            webbrowser.open(f"https://www.google.com/search?q={command}")

# Run the assistant
mini_jarvis()
