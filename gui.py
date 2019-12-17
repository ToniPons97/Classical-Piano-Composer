import tkinter as tk
from tkinter import ttk
from os import listdir
from os.path import isfile, join



midi_files = [f for f in listdir("./midi_songs2") if isfile(join("./midi_songs2", f))]

sound_fonts = [f for f in listdir("../../.fluidsynth") if isfile(join("../../.fluidsynth", f))]



app = tk.Tk() 
app.geometry('370x370')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboMidis = ttk.Combobox(app, 
                            values = midi_files)
comboMidis.grid(column=0, row=1)
comboMidis.current(1)

comboSoundFonts = ttk.Combobox(app, 
                            values = sound_fonts)
comboSoundFonts.grid(column=1, row=1)
comboSoundFonts.current(1)


app.mainloop()

