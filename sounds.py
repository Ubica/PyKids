import os
import random

from pydub import AudioSegment
from simpleaudio import WaveObject

PYDUB = 'pydub'
SIMPLEAUDIO = 'simpleaudio'


class Sounds():
    def __init__(self, audio_library):
        self.sounds = {}
        folder = 'sounds'
        language = 'srb'
        path = os.path.join(folder, language)

        for root, dirs, files in os.walk(path):
            if len(dirs) == 0:
                values = os.path.split(root)
                letter = values[0][-1]
                t = values[1]
                for file in files:
                    filepath = os.path.join(root, file)
                    if file[-3:] != 'wav':
                        os.remove(filepath)
                        continue
                    if letter not in self.sounds:
                        self.sounds[letter] = {}
                    if t not in self.sounds[letter]:
                        self.sounds[letter][t] = []

                    if audio_library == PYDUB:
                        sound_object = AudioSegment.from_file(filepath, format="wav")
                    elif audio_library == SIMPLEAUDIO:
                        sound_object = WaveObject(
                            open(filepath, 'rb').read(),
                            num_channels=1,
                            bytes_per_sample=2,
                            sample_rate=44100
                        )
                    else:
                        raise Exception('audio_library not configured')

                    self.sounds[letter][t].append(sound_object)

    def get_random_sound(self, letter):
        if letter in self.sounds and 'letter' in self.sounds[letter]:
            index = random.randint(0, len(self.sounds[letter]['letter']) - 1)
            return self.sounds[letter]['letter'][index]

    def get_random_word(self, letter):
        if letter in self.sounds and 'words' in self.sounds[letter]:
            index = random.randint(0, len(self.sounds[letter]['words']) - 1)
            return self.sounds[letter]['words'][index]
