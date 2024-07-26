import pygame

def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image.convert_alpha()

def load_sprite_sheet(filename, frame_width, frame_height):
    sheet = load_image(filename)
    sheet_rect = sheet.get_rect()
    sprites = []
    for y in range(0, sheet_rect.height, frame_height):
        for x in range(0, sheet_rect.width, frame_width):
            frame = sheet.subsurface((x, y, frame_width, frame_height))
            sprites.append(frame)
    return sprites

def get_time():
    return pygame.time.get_ticks()
