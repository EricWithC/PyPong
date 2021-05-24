import pygame as pg
import random
from . import setup

class Ball(pg.sprite.Sprite):
    def __init__(self, screen_rect, color=(255, 255, 255)):
        super().__init__()
        self.screen_rect = screen_rect
        self.image = pg.Surface((20, 20))
        self.set_color(color)
        self.speed = [5, 5]
        self.reset_position()

    def set_color(self, color):
        self.image.fill(color)

    def reset_position(self):
        self.rect = self.image.get_rect(
            center=(self.screen_rect.centerx, self.screen_rect.centery)
        )
        self.speed[0] = self.speed[0] * self.change_direction()[0]

    def change_direction(self):
        x = random.choice((-1, 1))
        y = random.choice((-1, 1))
        return (x, y)
    
    def move(self, paddles):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.y > setup.SCREEN_RECT.height or self.rect.y < 0:
            self.speed[1] = -self.speed[1]
        if pg.sprite.collide_mask(self, paddles[0]) or pg.sprite.collide_mask(self, paddles[1]):
            self.bounce()

    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.set_color((random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)))

    def update(self, paddles, score_labels):
        self.move(paddles)
        if self.rect.x > setup.SCREEN_RECT.width:
            self.reset_position()
            paddles[0].score += 1
            score_labels[0].update(paddles[0].score)
        elif self.rect.x < 0:
            self.reset_position()
            paddles[1].score += 1
            score_labels[1].update(paddles[1].score)

    def draw(self, surf):
        surf.blit(self.image, self.rect)