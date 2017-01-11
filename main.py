from threading import Thread
from tkinter import Canvas, Tk, font

from sounds import Sounds


class Kids():
    def __init__(self):
        self.master = Tk()

        self.canvas = Canvas(self.master)
        self.canvas.pack(fill='both', expand='yes')
        x, y = self.getCenter(self.canvas)
        self.sounds = Sounds()
        self.playing = False
        self.c = self.canvas.create_text(x, y, text='')

        def key(event):
            global c, for_playing, sounds
            key = event.char.lower()
            if key in 'abcdefghijklmnopqrstuvwxyz123456789' and not self.playing:
                playlist = []
                self.canvas.delete(self.c)
                x, y = self.getCenter(self.canvas)
                self.c = self.canvas.create_text(x, y, text=key.upper(), font=self.getFont(self.canvas))
                letter = self.sounds.getRandomSound(key)
                word = self.sounds.getRandomWord(key)
                if word:
                    playlist.append(word)
                if letter:
                    playlist.append(letter)
                t = Thread(target=self.play_thread, args=[playlist])
                t.setDaemon(True)
                t.start()

        self.master.bind('<Key>', key)

        self.master.mainloop()

    def width(self, canvas):
        return canvas.winfo_width()

    def height(self, canvas):
        return canvas.winfo_height()

    def getCenter(self, canvas):
        y = int(self.height(canvas) / 2)
        x = int(self.width(canvas) / 2)
        return x, y

    def getFont(self, canvas):
        return font.Font(family='Arial', size=int(self.height(canvas) * 0.6))

    def play_thread(self, playlist):
        self.playing = True
        while(playlist):
            item = playlist.pop()
            item.play().wait_done()
        self.playing = False


def main():
    Kids()


if __name__ == '__main__':
    main()
