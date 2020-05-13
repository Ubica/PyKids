from threading import Thread
from tkinter import Canvas, Tk, font

from pydub import AudioSegment
from pydub.playback import play
from simpleaudio import WaveObject
import sounds


class Kids:
    def __init__(self):
        self.master = Tk()

        self.canvas = Canvas(self.master)
        self.canvas.pack(fill='both', expand='yes')
        x, y = self.get_center(self.canvas)

        # Sound configuration
        self.sounds = sounds.Sounds(audio_library=sounds.PYDUB)
        self.playing = False
        self.c = self.canvas.create_text(x, y, text='')
        self.counter = 0

        def key(event):
            key_press = event.char.lower()
            if key_press in 'abcdefghijklmnopqrstuvwxyz123456789' and not self.playing:
                playlist = []
                self.canvas.delete(self.c)
                text_x, text_y = self.get_center(self.canvas)
                self.c = self.canvas.create_text(
                    text_x,
                    text_y,
                    text=f'{key_press.upper()} {key_press.lower()}',
                    font=self.get_font(self.canvas),
                )
                letter = self.sounds.get_random_sound(key_press)
                word = self.sounds.get_random_word(key_press)
                if word:
                    playlist.append(word)
                if letter:
                    playlist.append(letter)
                t = Thread(target=self.play_thread, args=[playlist])
                t.setDaemon(True)
                t.start()

        self.master.bind('<Key>', key)

        self.master.mainloop()

    @staticmethod
    def width(canvas):
        return canvas.winfo_width()

    @staticmethod
    def height(canvas):
        return canvas.winfo_height()

    def get_center(self, canvas):
        y = int(self.height(canvas) / 2)
        x = int(self.width(canvas) / 2)
        return x, y

    def get_font(self, canvas):
        # # Font family debug
        # families = font.families()
        # family = families[self.counter % len(families)]
        # self.counter += 1
        # print(family)
        return font.Font(family='Chalkboard', size=int(self.height(canvas) * 0.6))

    def play_thread(self, playlist):
        self.playing = True
        while playlist:
            item = playlist.pop()
            if isinstance(item, WaveObject):
                item.play().wait_done()
            elif isinstance(item, AudioSegment):
                play(item)
        self.playing = False


def main():
    Kids()


if __name__ == '__main__':
    main()
