from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = "en"
speech = gTTS(text="Hello PYTHON, How are you doing?",lang=language,slow=True)
speech.save(audio)
playsound(audio)
print("==audio is playing==")