from tkinter import Canvas, Tk, font

import simpleaudio as sa
from sounds import Sounds


def width(canvas):
    return canvas.winfo_width()

def height(canvas):
    return canvas.winfo_height()

def getCenter(canvas):
    y = int(height(canvas) / 2)
    x = int(width(canvas) / 2)
    return x, y

def getFont(canvas):
    return font.Font(family='Arial', size=int(height(canvas) * 0.6))

def main():
    master = Tk()

    canvas = Canvas(master)
    canvas.pack(fill='both', expand='yes')

    x, y = getCenter(canvas)
    global c, playing, sounds
    sounds = Sounds()
    playing = None
    c = canvas.create_text(x, y, text='')

    def key(event):
        global c, playing, sounds
        key = event.char.lower()
        if key in 'abcdefghijklmnopqrstuvwxyz123456789' and (not playing or not playing.is_playing()):
            canvas.delete(c)
            x, y = getCenter(canvas)
            c = canvas.create_text(x, y, text=key.upper(), font=getFont(canvas))
            letter = sounds.getRandomSound(key)
            word = sounds.getRandomWord(key)
            audio_data = None
            if letter and word:
                audio_data = letter + word
            elif letter:
                audio_data = letter
            elif word:
                audio_data = word
            if audio_data:
                playing = sa.play_buffer(audio_data, 1, 2, 44100)

    master.bind('<Key>', key)

    master.mainloop()

if __name__ == '__main__': main()
