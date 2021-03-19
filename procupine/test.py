import pvporcupine
import struct
import pyaudio
import time

handle = pvporcupine.create(keyword_paths=['./hey_diego_linux_2021-04-17-utc_v1_9_0.ppn'])


pa = pyaudio.PyAudio()
audio_stream = pa.open(
                rate=handle.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=handle.frame_length)
while True:
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    keyword_index = handle.process(pcm)
    if keyword_index >= 0:
        print("Wake Word Detected")
        # wait for 3 seconds - pretend doing other stuff
        # maybe I should be looking into event and multi-threading in Python
        time.sleep(3);
        break;

handle.delete();
