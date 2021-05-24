import pygame as pg
import random
from . import paddle, setup

class Rival(paddle.Paddle):
    def __init__(self, screen_rect, color=(255, 255, 255)):
        super().__init__(screen_rect)
        self.screen_rect = screen_rect
        self.set_color(color)

    def update(self, keys, ball):
        self.rect.clamp_ip(self.screen_rect)
        if ball.rect.y > self.rect.y:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        # if keys[pg.K_DOWN]:
        #     self.rect.y += self.speed
        # if keys[pg.K_UP]:
        #     self.rect.y -= self.speed