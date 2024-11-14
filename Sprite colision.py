import pygame
import random

SCREEN_WIDTH,SCREEN_HIEGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background-image = 
pygame.transform.scale(pygame.image.load("bg.jpg"),(SCREEN_HIEGHT, SCREEN_WIDTH))

font = pygame.font.SysFont("Times New Roman",FONT_SIZE)

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, hieght, width):
        super().__init__()
        self.image = pygame.Surface([width, hieght])
        self.image.fill(pygame.Color('Dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, hieght))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HIEGHT - self.rect.height), 0)

        screen = pygame.display.setmodal((SCREEN_WIDTH, SCREEN_HIEGHT))
        pygame.display.set_caption("Sprite Collision")
        all_sprite = pygame.sprite.Group()

        sprite1 = Sprite(pygame.Colr("black"), 20, 30)
        sprite1.rect.x, sprite.rect.y = random.int