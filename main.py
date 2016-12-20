from tkinter import Canvas, Tk, font

import simpleaudio as sa


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
    global c, playing
    playing = None
    c = canvas.create_text(x, y, text='')

    def key(event):
        global c, playing
        key = event.char
        canvas.delete(c)
        x, y = getCenter(canvas)
        c = canvas.create_text(x, y, text=key.upper(), font=getFont(canvas))
        if key == 'a':
            if not playing:
                audio_data = open('a.wav', 'rb').read()
                playing = sa.play_buffer(audio_data, 2, 2, 44100)
        if key == 'b':
            if playing and playing.is_playing():
                playing.stop()
            playing = None

    master.bind('<Key>', key)

    master.mainloop()

if __name__ == '__main__': main()
