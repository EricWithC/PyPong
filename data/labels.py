import pygame as pg
from . import tools

class Label:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.font_init(self.screen_rect)

    def font_init(self, screen_rect):
        self.text_size = 50
        self.text_color = (255, 255, 255)
        self.font = tools.Font.load('8bitOperatorPlus-Regular.ttf', self.text_size)

    def make_text(self, message, pos):
        text = self.font.render(message, True, self.text_color)
        rect = text.get_rect(topleft=pos)
        return text, rect

    def draw(self):
        pass

class GameOverText(Label):
    def __init__(self, screen_rect):
        super().__init__(screen_rect)
        self.screen_rect = screen_rect
        self.game_over()

    def draw(self, surf):
        surf.blit(self.game_over_text, self.game_over_rect)

    def game_over(self):
        game_over_font = tools.Font.load('8bitOperatorPlus-Regular.ttf', 45)
        self.game_over_text = game_over_font.render('Game Over', True, (255, 0, 0))
        self.game_over_rect = self.game_over_text.get_rect(center=self.screen_rect.center)

class ScoreText(Label):
    def __init__(self, pos, msg, arg, screen_rect):
        super().__init__(screen_rect)
        self.pos = pos
        self.msg = msg
        self.update()

    def update(self, arg=0):
        self.score, self.score_rect = self.make_text(self.msg.format(arg), self.pos)

    def draw(self, surf):
        surf.blit(self.score, self.score_rect)