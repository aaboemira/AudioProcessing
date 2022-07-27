import pyaudio
import wave
import sys


def play_audio(frame_rate, filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=int(frame_rate * wf.getframerate()),
                    output=True)

    data = wf.readframes(chunk)

    print("[+] Playing audio. To terminate, press CTRL+C")
    
    while data != b'':
        try:
            stream.write(data)
            data = wf.readframes(chunk)
        except KeyboardInterrupt:
            sys.exit(-1)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
