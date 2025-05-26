import pygame
from map import TILE_SIZE, BANK_MAP 

class Player:
    def __init__(self, x, y, color=(0, 200, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.size = TILE_SIZE // 2

    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        # Wall collision
        if BANK_MAP[ny][nx] == 0:
            self.x, self.y = nx, ny

    def draw(self, surface):
        px = self.x * TILE_SIZE + TILE_SIZE // 4
        py = self.y * TILE_SIZE + TILE_SIZE // 4
        pygame.draw.rect(surface, self.color, (px, py, self.size, self.size))