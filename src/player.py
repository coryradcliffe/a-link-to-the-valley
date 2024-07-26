import pygame
from animation import Animation
from assets_loader import load_sprite_sheet
from settings import PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load_animations()
        self.image = self.idle_animation.get_frame()
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.speed = PLAYER_SPEED
        self.current_animation = self.idle_animation

    def load_animations(self):
        idle_frames = load_sprite_sheet('characters/player.png', 48, 48)[0:6]
        move_frames = load_sprite_sheet('characters/player.png', 48, 48)[18:24]
        attack_frames = load_sprite_sheet('characters/player.png', 48, 48)[36:42]

        self.idle_animation = Animation(idle_frames, 100)
        self.move_animation = Animation(move_frames, 100)
        self.attack_animation = Animation(attack_frames, 100)

    def update(self, dt):
        self.current_animation.update(dt)
        self.image = self.current_animation.get_frame()
        self.handle_input()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.current_animation = self.move_animation
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.current_animation = self.move_animation
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.current_animation = self.mov
