import os
import random
from simpleaudio import WaveObject

class Sounds():
    def __init__(self):
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
                    if file[-3:] != 'wav': # cleanup
                        os.remove(filepath)
                        continue
                    if letter not in self.sounds:
                        self.sounds[letter] = {}
                    if t not in self.sounds[letter]:
                        self.sounds[letter][t] = []
                    zvukData = open(filepath, 'rb').read()
                    zvukObject = WaveObject(zvukData, num_channels=1, bytes_per_sample=2, sample_rate=44100)
                    self.sounds[letter][t].append(zvukObject)
                    
    def getRandomSound(self, letter):
        if letter in self.sounds and 'letter' in self.sounds[letter]:
            index = random.randint(0, len(self.sounds[letter]['letter']) - 1)
            return self.sounds[letter]['letter'][index]
    
    def getRandomWord(self, letter):
        if letter in self.sounds and 'words' in self.sounds[letter]:
            index = random.randint(0, len(self.sounds[letter]['words']) - 1)
            return self.sounds[letter]['words'][index]