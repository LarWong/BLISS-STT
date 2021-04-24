import pvporcupine
import struct
import pyaudio
import time
import requests
import torch
import sounddevice as sd
import numpy
import json

class WakeWord():
    def __init__(self, pv_model='./hey_diego_linux_2021-05-23-utc_v1_9_0.ppn',
                       speech_url='http://127.0.0.1:5000/speech',
                       status_url='http://127.0.0.1:5000/status'):
        self.handle = pvporcupine.create(
                    keyword_paths=[
                    pv_model
                    ])
        # Hey computer for the time being
        #self.handle = pvporcupine.create(keywords=['computer'])
        # Need to update this with an actual address
        self.url = speech_url
        self.status_url = status_url
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
                        rate=self.handle.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.handle.frame_length)
        # Download dependencies
        self.synthesizer = torch.hub.load('coqui-ai/TTS:dev', 'tts', source='github')
    
    def speak(self, output_text):
        wav = self.synthesizer.tts(output_text)
        sd.play(wav, self.synthesizer.ap.sample_rate)
        sd.wait()

    def run(self):
        while True:
            pcm = self.audio_stream.read(self.handle.frame_length)
            pcm = struct.unpack_from("h" * self.handle.frame_length, pcm)
            keyword_index = self.handle.process(pcm)
            if keyword_index >= 0:
                print("Wake Word Detected")

                response = None

                # check if connection to server is established
                try:
                    response = requests.get(self.status_url)
                except:
                    print('Error from server')
                
                if not response:
                    self.speak('Sorry. No connection to server. Please try again.')
                    continue

                self.speak('How may I help you?')
                print("DeepSpeech Activated")

                # send post request to the flask server
                try:
                    response = requests.get(self.url)
                except:
                    print('Error from server')

                transcribed_text = response.text if response else 'Sorry, something went wrong. Please try again'
                # Text might not be a string
                payload = {
                    'sender':'test',
                    'message':transcribed_text
                }
                headers = {
                    'content-type': 'application/json'
                }
                # Send it over to RASA
                response_rasa = requests.post('http://localhost:5005/webhooks/rest/webhook', json = payload, headers = headers)
                # print(response_rasa.text)
                feedback = json.loads(response_rasa.content) if response_rasa else 'Sorry, I could not reach the server. Please try again'
                # Invoke TTS
                self.speak(feedback[0]['text'])
                                   

def main():
    Listener = WakeWord()
    Listener.run()

if __name__ == '__main__':
    main()
