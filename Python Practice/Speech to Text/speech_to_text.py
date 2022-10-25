import pyaudio
import wave
import speech_recognition as sr

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 5
filename = "/Users/robinmohanty/Desktop/Study/Speech_To_Text/output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()


filename = "/Users/robinmohanty/Desktop/Study/Speech_To_Text/output.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
	# listen for the data (load audio to memory)
	audio_data = r.record(source)
	# recognize (convert from speech to text)
	text = r.recognize_google(audio_data)
	print(text)
	file = open("/Users/robinmohanty/Desktop/Study/Speech_To_Text/Speech_To_text.txt","w")
	file.write(text)
