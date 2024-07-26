import pygame
from player import Player
from enemy import Enemy
from tilemap import TileMap
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.enemies = pygame.sprite.Group()
        self.create_enemies()
        self.tilemap = TileMap('flooring.png')

    def create_enemies(self):
        enemy = Enemy('skeleton.png', 48, 48)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.all_sprites.update(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tilemap.draw(self.screen)
        self.all_sprites.draw(self.screen)
