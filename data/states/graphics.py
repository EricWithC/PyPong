import pygame as pg
from .. import tools, labels, setup, menu_manager, player, rival

class Graphics(tools.States, menu_manager.MenuManager):
    def __init__(self):
        tools.States.__init__(self)
        menu_manager.MenuManager.__init__(self)
        self.next = 'game'
        self.options = ['Back']
        self.next_list = ['options']
        self.pre_render_options()
        self.from_bottom = 175
        self.spacer = 75

    def cleanup(self):
        print('Cleaning up Menu state stuff')
    
    def startup(self):
        print('Starting Menu state stuff')

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.get_event_menu(event)
    
    def update(self, screen, keys):
        self.update_menu()
        self.draw(screen)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_menu()