import pygame
from animation import Animation
from assets_loader import load_sprite_sheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_file, frame_width, frame_height):
        super().__init__()
        self.load_animations(sprite_file, frame_width, frame_height)
        self.image = self.idle_animation.get_frame()
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 200)
        self.current_animation = self.idle_animation

    def load_animations(self, sprite_file, frame_width, frame_height):
        idle_frames = load_sprite_sheet('characters/' + sprite_file, frame_width, frame_height)[0:18]
        move_frames = load_sprite_sheet('characters/' + sprite_file, frame_width, frame_height)[18:36]
        attack_frames = load_sprite_sheet('characters/' + sprite_file, frame_width, frame_height)[36:54]
        damaged_frames = load_sprite_sheet('characters/' + sprite_file, frame_width, frame_height)[54:72]
        death_frames = load_sprite_sheet('characters/' + sprite_file, frame_width, frame_height)[72:78]

        self.idle_animation = Animation(idle_frames, 100)
        self.move_animation = Animation(move_frames, 100)
        self.attack_animation = Animation(attack_frames, 100)
        self.damaged_animation = Animation(damaged_frames, 100)
        self.death_animation = Animation(death_frames, 100)

    def update(self, dt):
        self.current_animation.update(dt)
        self.image = self.current_animation.get_frame()
