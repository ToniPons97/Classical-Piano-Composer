import tkinter as tk
from tkinter import ttk
from os import listdir
from os.path import isfile, join
from main import generate_wav

midi_root = "./midi_songs2"
sound_font_root = "../../.fluidsynth"

midi_files = [f for f in listdir(midi_root) if isfile(join(midi_root, f))]

sound_fonts = [f for f in listdir(sound_font_root) if isfile(join(sound_font_root, f))]



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
    


comboMidis.bind("<<ComboboxSelected>>", callbackMidi)
comboSoundFonts.bind("<<ComboboxSelected>>", callbackSoundFont)

btn = ttk.Button(app, text="Generate WAV", command=generate_wav_btn)
btn.grid(column=0, row=2)


app.mainloop()


