import pygame as pg
from .. import (
    tools,
    labels,
    menu_manager,
    setup,
    player,
    rival,
    ball
)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = 'lightskyblue3'
        self.text = text
        self.font = tools.Font.load('8bitOperatorPlus-Regular.ttf', 20)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = 'dodgerblue2' if self.active else 'lightskyblue3'
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                   return self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

class Game(tools.States, menu_manager.MenuManager):
    def __init__(self):
        tools.States.__init__(self)
        menu_manager.MenuManager.__init__(self)
        self.next = 'game_over'
        self.player_score = labels.ScoreText((250, 10), '{}', 0, setup.SCREEN_RECT)
        self.rival_score = labels.ScoreText((750, 10), '{}', 0, setup.SCREEN_RECT)
        self.player = player.Player(setup.SCREEN_RECT)
        self.rival = rival.Rival(setup.SCREEN_RECT)
        self.ball = ball.Ball(setup.SCREEN_RECT)
        self.input_player_color = InputBox(100, 100, 50, 50)
        self.input_rival_color = InputBox(300, 100, 50, 50)
        self.input_ball_color = InputBox(200, 200, 50, 50)

    def restart(self):
        self.ball.reset_position()
        self.player.reset_position()
        self.rival.reset_position()
    
    def cleanup(self):
        print('Cleaning up Game state stuff')
        self.restart()
    
    def startup(self):
        print('Starting Game state stuff')

    def get_event(self, event):
        self.input_player_color.handle_event(event)
        self.input_rival_color.handle_event(event)
        self.input_ball_color.handle_event(event)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.player.set_color(self.input_player_color.handle_event(event))
                self.rival.set_color(self.input_rival_color.handle_event(event))
                self.ball.set_color(self.input_ball_color.handle_event(event))
    
    def update(self, screen, keys):
        self.draw(screen)
        self.input_player_color.update()
        self.input_rival_color.update()
        self.input_ball_color.update()
        # self.player.update(keys)
        # self.rival.update(keys, self.ball)
        # self.ball.update((self.player, self.rival), (self.player_score, self.rival_score))
        # if self.player.score >= 10 or self.rival.score >= 10:
        #     self.done = True

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.input_player_color.draw(screen)
        self.input_rival_color.draw(screen)
        self.input_ball_color.draw(screen)
        self.middle_line = pg.Surface((20, setup.SCREEN_RECT.height))
        self.middle_line.fill((255, 255, 255))
        screen.blit(self.middle_line, (setup.SCREEN_RECT.centerx - 10, 0))
        self.player_score.draw(setup.SCREEN)
        self.rival_score.draw(setup.SCREEN)
        self.player.draw(setup.SCREEN)
        self.rival.draw(setup.SCREEN)
        self.ball.draw(setup.SCREEN)
        