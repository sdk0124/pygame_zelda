import pygame, os
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '../graphics/test/rock.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
