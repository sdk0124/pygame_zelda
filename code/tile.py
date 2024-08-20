import pygame, os
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups) # 해당 객체 생성 시 인자로 넘겨진 그룹으로 추가됨.
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '../graphics/test/rock.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
