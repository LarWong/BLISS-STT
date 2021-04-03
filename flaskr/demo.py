import pvporcupine
import struct
import pyaudio
import time
import requests

class WakeWord():
    def __init__(self):
        self.handle = pvporcupine.create(
                    keyword_paths=[
                    './hey_diego_linux_2021-04-17-utc_v1_9_0.ppn'
                    ])
        # Need to update this with an actual address
        self.url = 'http://127.0.0.1:5000/speech'
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
                        rate=self.handle.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.handle.frame_length)
        self.sleep_time = 10
    
    def run(self):
        while True:
            pcm = self.audio_stream.read(self.handle.frame_length)
            pcm = struct.unpack_from("h" * self.handle.frame_length, pcm)
            keyword_index = self.handle.process(pcm)
            if keyword_index >= 0:
                print("Wake Word Detected")
                print("DeepSpeech Activated")
                # wait for 10 seconds
                # send post request to the flask server
                requests.get(self.url)
                time.sleep(self.sleep_time)
                break
    
    def delete(self):
        self.handle.delete()

def main():
    Listener = WakeWord()
    Listener.run()
    Listener.delete()

if __name__ == '__main__':
    main()
