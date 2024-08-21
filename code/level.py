# level setting
import pygame, os, random
from setting import *
from tile import Tile
from player import Player
from support import import_csv_layout, import_folder
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
        base_path = os.path.dirname(__file__)
        boundary_path = os.path.join(base_path, '../map/map_FloorBlocks.csv')
        map_grass_path = os.path.join(base_path, '../map/map_Grass.csv')
        objects_path = os.path.join(base_path, '../map/map_Objects.csv')
        layouts = {
            'boundary' : import_csv_layout(boundary_path),
            'grass': import_csv_layout(map_grass_path),
            'object': import_csv_layout(objects_path)
        }

        graphics_grass_path = os.path.join(base_path, '../graphics/grass')
        graphics_objects_path = os.path.join(base_path, '../graphics/objects')
        graphics = {
            'grass' : import_folder(graphics_grass_path),
            'objects' : import_folder(graphics_objects_path)
        }
        print(graphics)

        for style, layout in layouts.items():
            for row_idx, row in enumerate(layout):
                for col_idx, col in enumerate(row):
                    if col != '-1': # -1 : 비어있음.
                        x = col_idx * TILESIZE
                        y = row_idx * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            grass_image_list = graphics['grass']
                            selected_grass_image = random.choice(grass_image_list)
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', selected_grass_image)                            
                        if style == 'object':
                            selected_object_image = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', selected_object_image)
        
        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites)
        
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

        # creating the floor
        base_path = os.path.dirname(__file__)
        floor_image_path = os.path.join(base_path, '../graphics/tilemap/ground.png')
        self.floor_surface = pygame.image.load(floor_image_path).convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw floor
        floor_offset_position = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_position)

        # draw sprites
        # sorted함수를 사용한 이유 : y좌표를 기준으로 정렬하여 y좌표가 더 큰 것이 나중에 그려져야 함.
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
