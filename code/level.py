# level setting
import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup() # 화면에 그려지는 모든 스프라이트들의 그룹
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
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        # debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # sorted함수를 사용한 이유 : y좌표를 기준으로 정렬하여 y좌표가 더 큰 것이 나중에 그려져야 함.
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
