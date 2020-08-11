import speech_recognition as sr
import moviepy.editor as mp

clip=mp.VideoFileClip(r'C:/Users/sansar/Downloads/Full Song- KHAIRIYAT (BONUS TRACK) - CHHICHHORE - Sushant, Shraddha - Pritam, Amitabh B-Arijit Singh.webm')
clip.audio.write_audiofile(r'converted.wav')

r=sr.Recognizer()

audio=sr.AudioFile('coverted.wav')

with audio as source:
    audio_file=r.record(source)

result=r.recognize_google(audio_file)

with open('recognized.txt',mode='w') as file:
    file.write('Recognized Speech:')

    file.write('\n')
    file.write(result)
    print('Ready!')
