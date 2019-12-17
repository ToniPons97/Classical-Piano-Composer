#!/usr/local/bin/python3
from midi2audio import FluidSynth
import subprocess
from pydub import AudioSegment
from pydub.playback import play


def generate_wav(midi_name, sound_font):
    """
    generate a wav file.
    Input arguments:
    sound_font: the sf2 file selected to make the audio.
    midi_name: the name of the midi file to be converted.
    wav_name: the name of the wav file to generate.
    """
    if type(sound_font) == list:
        for i in sound_font:
            wav_file = f"{midi_name}-{i}.wav"
            print(f"Generating {wav_file}")
            FluidSynth(f"~/.fluidsynth/{i}").midi_to_audio(f"./midi_songs2/{midi_name}", f"./wav_output/{wav_file}")
    elif type(sound_font) == str:
        FluidSynth(f"~/.fluidsynth/{sound_font}").midi_to_audio(
            f"./midi_songs2/{midi_name}", 
            f"./wav_output/{midi_name}-{sound_font}.wav")





def mix_wavs(wav_name1, wav_name2):
    """
    generate mp3 file with all wavs added.
    """
    sound1 = AudioSegment.from_mp3(f"./wav_output/{wav_name1}")
    sound2 = AudioSegment.from_mp3(f"./wav_output/{wav_name2}")

    # mix sound2 with sound1, starting at position=0 ms into sound1)
    output = sound1.overlay(sound2)

    # save the result
    output.export("./wav_output/mixed_sounds.mp3", format="mp3")
    print(f"generated mp3 file!")

def play_audio(file_name):
    ext = file_name.split(".")[-1]
    print(f"Playing {ext} file...")
    print("Press CTRL + C to stop.")
    try:
        sound = AudioSegment.from_file(f"./wav_output/{file_name}", format=ext)
        play(sound)
    except KeyboardInterrupt:
        print("Quit")


#generate_wav("01minuet.mid", ["Pianino.sf2", "RolandMarcatoStrings.sf2"])


#generate_wav("01minuet.mid", "RolandMarcatoStrings.sf2")


#play_audio("01minuet.mid-Pianino.sf2.wav")