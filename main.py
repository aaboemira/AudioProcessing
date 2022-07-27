from record_audio import record
from play_audio import play_audio
from speech_to_text import voice_to_text, audio_to_text
import sys


def main():
    usage = '''[-] Usage: python main.py <mode_number> <mode_arguments>
    Modes:
        1: record an audio, arguments: <duration> <file_name>
        2: play an audio, arguments: <speed_rate> <file_name>
        3: record and play, arguments: <duration> <speed_rate> <file_name>
        4: voice-to-text, arguments: <duration>
        5: audio-to-text, arguments: <file_name>
    '''
    if len(sys.argv) < 3:
        print(usage)
        sys.exit(-1)

    mode = int(sys.argv[1])
    if mode == 1:
        record(int(sys.argv[2]), sys.argv[3])
    elif mode == 2:
        play_audio(float(sys.argv[2]), sys.argv[3])
    elif mode == 3:
        record(int(sys.argv[2]), sys.argv[4])
        play_audio(int(sys.argv[3]), sys.argv[4])
    elif mode == 4:
        voice_to_text(int(sys.argv[2]))
    elif mode == 5:
        audio_to_text(sys.argv[2])
    else:
        print("[-] There is no such mode")
        print(usage)


if __name__ == '__main__':
    main()
