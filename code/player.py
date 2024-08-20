import pygame, os
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups) # 해당 객체 생성 시 인자로 넘겨진 그룹으로 추가됨.
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '../graphics/test/player.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        # horizontal direction
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0 # 키를 누르고 있지 않으면 0

        # vertical direction
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0 # 키를 누르고 있지 않으면 0

    def move(self, speed): # 코드의 재사용성을 높이기 위해 speed를 argument로 넘김
        # 대각선의 경우 self.direction 벡터 크기가 1보다 큼.
        # 어떤 방향으로 움직이든 간에 벡터 크기를 1로 하고 싶다.
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)