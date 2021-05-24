import os
import pygame as pg

class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previoue = None

class Font:
    path = 'resources/fonts'
    @staticmethod
    def load(filename, size):
        p = os.path.join(Font.path, filename)
        return pg.font.Font(os.path.abspath(p), size)

class Sound:
    def __init__(self, filename):
        self.path = os.path.join('resources', 'sounds')
        self.fullpath = os.path.join(self.path, filename)
        pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=128)
        self.sound = pg.mixer.Sound(os.path.abspath(self.fullpath))

def load_all_sfx(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    '''
    Load all sfx with extensions found in accept. Unfortunately it is
    common to need to set sfx volume on a one-by-one basis. This must be done
    manually if necessary in the setup module.
    '''
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))

    return effects

def load_all_gfx(directory, colorkey=(0, 0, 0), accept=(".png", ".jpg", ".bmp")):
    '''
    Load all gfx with extensions found in accept. If alpha 
    transparency is found in the image, the image will be converted
    using convert_alpha(). Otherwise convert() will be used and
    colorkey will be set to given colorkey.
    '''
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img

    return graphics