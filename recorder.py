import sounddevice
from scipy.io.wavfile import write

def record():
    fs = 44100
    second = int(input('Enter the time duration in second: '))
    print('Recording...')
    record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write('out.wav',fs,record_voice)
    print('Finished')

if __name__ == "__main__":
    record()