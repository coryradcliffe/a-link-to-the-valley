import pygame
import os

class TileMap:
    def __init__(self, filename):
        self.tile_size = 32
        self.tiles = self.load_tiles(filename)
        self.map_data = self.load_map(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tilesets', 'map.txt'))

    def load_tiles(self, filename):
        # Correctly resolve the path to the tileset file
        tileset_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tilesets', filename)
        try:
            tileset = pygame.image.load(tileset_path).convert()
        except pygame.error as message:
            print(f"Cannot load tileset image: {tileset_path}")
            raise SystemExit(message)
        tiles = []
        for y in range(0, tileset.get_height(), self.tile_size):
            for x in range(0, tileset.get_width(), self.tile_size):
                tile = tileset.subsurface((x, y, self.tile_size, self.tile_size))
                tiles.append(tile)
        return tiles

    def load_map(self, filename):
        try:
            with open(filename, 'r') as f:
                map_data = f.readlines()
        except IOError as e:
            print(f"Cannot load map file: {filename}")
            raise SystemExit(e)
        return map_data

    def draw(self, screen):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles.strip()):
                if tile != '.':
                    screen.blit(self.tiles[int(tile)], (col * self.tile_size, row * self.tile_size))
