import requests
import json
import pyaudio
import speech_recognition as sr
import youtubesearchpython
import vlc
import pyttsx3
import pafy
import time
import struct
import youtubePython
import pvporcupine

def get():
    response=requests.get('https://jsonblob.com/api/jsonBlob/f70ef30b-85bc-11eb-9929-6fbc47681238')
    print(response.json()['message'])

def putMethod():
    porcupine = pvporcupine.create(keywords=["computer", "jarvis"])
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)
    while True:

        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            r = sr.Recognizer()
            mic = sr.Microphone()
            engine = pyttsx3.init()
            with mic as source:
                engine.setProperty('volume',1.0)
                engine.say("Listening")
                engine.runAndWait()

                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                
                saidText = r.recognize_google(audio)
                engine.stop()
                myjson = {
                    "message":saidText
                }

                r = requests.put('https://jsonblob.com/api/jsonBlob/f70ef30b-85bc-11eb-9929-6fbc47681238', data=json.dumps(myjson, indent=4))

                if 'play' in saidText:
                    youtubePython.playSongInternet(saidText[5:])

        else:
            continue
    
putMethod()