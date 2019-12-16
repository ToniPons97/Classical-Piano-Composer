from pydub import AudioSegment

def mix_wavs():
    sound1 = AudioSegment.from_mp3("./wav_output/example1.wav")
    sound2 = AudioSegment.from_mp3("./wav_output/example2.wav")
    sound3 = AudioSegment.from_mp3("./wav_output/example3.wav")
    sound4 = AudioSegment.from_mp3("./wav_output/example4.wav")



    # mix sound2 with sound1, starting at position=0 ms into sound1)
    output = sound1.overlay(sound2).overlay(sound3).overlay(sound4)


    # save the result
    output.export("./wav_output/mixed_sounds.mp3", format="mp3")
    return f"generated mp3 file!"


mix_wavs()