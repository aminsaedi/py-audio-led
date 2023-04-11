import pyaudio
import numpy as np
import time

# Set up PyAudio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Audio processing function
def process_audio(data):

    if data is None:
        return False

    # Convert data to numpy array
    data = np.fromstring(data, dtype=np.int16)

    # Calculate the average volume
    volume = np.average(np.abs(data))

    # If the volume is above the threshold, return True
    if volume > 1000:
        return True
    else:
        return False



# Light control function
def control_light(on):
    if on:
        print("ON")
    else:
        print("OFF")

# Main loop
while True:
    data = stream.read(CHUNK)
    on = process_audio(data)
    control_light(on)
    time.sleep(0.02) # Set the loop frequency

