from gtts import gTTS
import os
import time

text = input("Введите текст: ")
audio = gTTS(text=text, lang="ru", slow=False)
audio.save('jj.mp3')
os.system('start jj.mp3')
