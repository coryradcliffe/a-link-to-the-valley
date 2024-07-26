import pygame
import os

def load_image(filename, colorkey=None):
    fullname = os.path.join(os.path.dirname(__file__), '..', 'assets', filename.replace('/', os.sep))
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print(f"Cannot load image: {fullname}")
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

def load_sprite_sheet(filename, frame_width, frame_height):
    sheet = load_image(filename)
    sheet_rect = sheet.get_rect()
    sprites = []
    for y in range(0, sheet_rect.height, frame_height):
        for x in range(0, sheet_rect.width, frame_width):
            frame = sheet.subsurface((x, y, frame_width, frame_height))
            sprites.append(frame)
    return sprites
