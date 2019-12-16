from midi2audio import FluidSynth
import subprocess
import argparse

def generate_wav(sound_font, midi_name, wav_name):
    """
    generate a wav file.
    Input arguments:
    sound_font: the sf2 file selected to make the audio.
    midi_name: the name of the midi file to be converted.
    wav_name: the name of the wav file to generate.
    """
    FluidSynth(f"~/.fluidsynth/{sound_font}").midi_to_audio(f"./midi_songs2/{midi_name}", f"./wav_output/{wav_name}.wav")
    return f"Generated {wav_name}"


def display_soundfonts():
    subprocess.run(["ls ~/.fluidsynth/"], shell=True)


#display_soundfonts()

generate_wav("Pyrex Strings.sf2", "01minuet.mid", "example1")
generate_wav("RolandMarcatoStrings.sf2", "01minuet.mid", "example2")
generate_wav("Strings Legato Korg Triton.SF2", "01minuet.mid", "example3")
generate_wav("Digital Sound Factory Examples Collection.SF2", "01minuet.mid", "example4")

