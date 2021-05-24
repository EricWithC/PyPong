import pygame as pg
from .. import (
    setup,
    tools, 
    labels, 
    menu_manager,
)

class GameOver(tools.States, menu_manager.MenuManager):
    def __init__(self):
        tools.States.__init__(self)
        menu_manager.MenuManager.__init__(self)
        self.next = 'main_menu'
        self.game_over_label = labels.GameOverText(setup.SCREEN_RECT)
    
    def cleanup(self):
        print('Cleaning up Game Over state stuff')
    
    def startup(self):
        print('Starting Game Over state stuff')

    def get_event(self, event):
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    
    def update(self, screen, keys):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.game_over_label.draw(screen)