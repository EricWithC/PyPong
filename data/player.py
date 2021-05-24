import pygame as pg
from . import paddle, setup

class Player(paddle.Paddle):
    def __init__(self, screen_rect, color=(255, 255, 255)):
        super().__init__(screen_rect)
        self.screen_rect = screen_rect
        self.set_color(color)
        self.set_x_position(-400)

    def reset_position(self):
        self.set_x_position(-400)

    def update(self, keys):
        self.rect.clamp_ip(self.screen_rect)
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_w]:
            self.rect.y -= self.speed