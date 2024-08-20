import pygame, os
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups) # 해당 객체 생성 시 인자로 넘겨진 그룹으로 추가됨.
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '../graphics/test/player.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

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

        # 자연스로운 충돌 확인을 위해 x, y 따로 구분
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

        # 이렇게 코드를 작성하면 방향키를 2개 눌렀을 때 밀려남.
        # self.rect.center += self.direction * speed
        # self.collision('horizontal')
        # self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    # 오른쪽으로 이동 중 충돌 : 장애물의 왼쪽 부분에 충돌했음
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left

                    # 왼쪽으로 이동 중 충돌 : 장애물의 오른쪽 부분에 충돌했음
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    # 아랫쪽으로 이동 중 충돌 : 장애물의 위쪽 부분에 충돌했음
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top

                    # 위쪽으로 이동 중 충돌 : 장애물의 아랫쪽 부분에 충돌했음
                    if self.direction.y < 0: # moving left
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)