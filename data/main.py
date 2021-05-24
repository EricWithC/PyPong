import pygame as pg
import sys
from . import setup
from .states import  game, main_menu, game_over, options, graphics

class Control:
    def __init__(self):
        self.done = False
        self.screen = setup.SCREEN
        self.clock = pg.time.Clock()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self):
        keys = pg.key.get_pressed()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, keys)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            self.clock.tick(setup.FPS)
            self.event_handler()
            self.update()
            pg.display.update()

app = Control()
state_dict = {
    'main_menu': main_menu.Menu(),
    'game':      game.Game(),
    'game_over': game_over.GameOver(),
    'options':   options.Options(),
    'graphics':  graphics.Graphics()
}
app.setup_states(state_dict, 'main_menu')
app.main_game_loop()
pg.quit()
sys.exit()            