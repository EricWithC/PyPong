import pygame as pg
from . import setup

class Paddle(pg.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        self.screen_rect = screen_rect
        self.image = pg.Surface((20, 100))
        self.set_color(color=(255, 255, 255))
        self.set_x_position(buffer=400)
        self.speed = 4
        self.score = 0

    def set_color(self, color):
        self.image.fill(color)

    def set_x_position(self, buffer):
        self.rect = self.image.get_rect(
            center=(self.screen_rect.centerx + buffer, self.screen_rect.centery)
        )

    def reset_position(self):
        self.set_x_position(buffer=400)

    def get_event(self, event):
        pass

    def update(self, keys):
        pass

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def add_score(self):
        self.score += 1
