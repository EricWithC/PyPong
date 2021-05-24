import os
import pygame as pg
from . import tools

CAPTION = "PyPong"
WINSIZE = (1000, 600)
FPS = 60

# Initialization
pg.init()

pg.display.set_caption(CAPTION)
SCREEN = pg.display.set_mode(WINSIZE)
SCREEN_RECT = SCREEN.get_rect()

# Load resources
SFX = tools.load_all_sfx(os.path.join('resources', 'sounds'))
GFX = tools.load_all_gfx(os.path.join('resources', 'images'))