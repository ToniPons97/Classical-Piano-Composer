import tkinter as tk
from tkinter import ttk
from os import listdir
from os.path import isfile, join
from main import generate_wav
from main import mix_wavs
import subprocess

midi_root = "./midi_songs2"
sound_font_root = "../../.fluidsynth"
wav_output_root = "./wav_output"

midi_files = [f for f in listdir(midi_root) if isfile(join(midi_root, f))]

sound_fonts = [f for f in listdir(sound_font_root) if isfile(join(sound_font_root, f))]
midi_files.remove(".DS_Store")


app = tk.Tk() 
app.geometry('520x370')

labelTop = tk.Label(app,
                    text = "Choose your favourite midi and fontsound")
labelTop.grid(column=0, row=0)

comboMidis = ttk.Combobox(app, 
                            values = midi_files, state="readonly")
comboMidis.grid(column=0, row=1)
comboMidis.current(1)

comboSoundFonts = ttk.Combobox(app, 
                            values = sound_fonts, state="readonly")
comboSoundFonts.grid(column=1, row=1)
comboSoundFonts.current(1)


midi_global = ""
sound_font_global = ""


def callbackMidi(eventObject):
    global midi_global
    midi_global = comboMidis.get()


def callbackSoundFont(eventObject):
    global sound_font_global
    sound_font_global = comboSoundFonts.get()
    

def generate_wav_btn():
    generate_wav(midi_global, sound_font_global)
    subprocess.run(["open", "./wav_output"])


def mix_wavs_btn():
    generated_wavs = [w for w in listdir(wav_output_root) if isfile(join(wav_output_root, w))]
    generated_wavs.remove(".DS_Store")

    mix_wavs(generated_wavs[-1], generated_wavs[-2])

def delete_all_files():
    subprocess.call(["rm ./wav_output/*"], shell=True)


comboMidis.bind("<<ComboboxSelected>>", callbackMidi)
comboSoundFonts.bind("<<ComboboxSelected>>", callbackSoundFont)

btn = ttk.Button(app, text="Generate WAV", command=generate_wav_btn)
btn.grid(column=0, row=2)


btn_mix = ttk.Button(app, text="Mix", command=mix_wavs_btn)
btn_mix.grid(column=0, row=3)

btn_del = ttk.Button(app, text="Delete all files", command=delete_all_files)
btn_del.grid(column=1, row=2)

app.mainloop()


