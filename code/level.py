# level setting
import pygame
from setting import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group() # 화면에 그려지는 모든 스프라이트들의 그룹
        self.obstacle_sprites = pygame.sprite.Group() # 플레이어와 충돌 가능한 모든 스프라이트들의 그룹

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_idx, row in enumerate(WORLD_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILESIZE
                y = row_idx * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    Player((x, y), [self.visible_sprites])
        
    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)