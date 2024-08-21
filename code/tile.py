import pygame, os
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups) # 해당 객체 생성 시 인자로 넘겨진 그룹으로 추가됨.
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '../graphics/test/rock.png')
        self.sprite_type = sprite_type
        self.image = surface
        
        # if type is object, objects can not be 64 x 64 size (usually more bigger)
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (position[0], position[1] - TILESIZE))
        else: # basic tile set
            self.rect = self.image.get_rect(topleft = position)

        self.hitbox = self.rect.inflate(0, -10) # hitbox 설정 (세로로 상 하 5px만큼 줄인다.)
