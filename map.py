import pygame

BANK_MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1],
    [1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

TILE_SIZE = 40

def draw_map(surface):
    for y, row in enumerate(BANK_MAP):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if cell == 1:
                pygame.draw.rect(surface, (80, 80, 80), rect)
            else:
                pygame.draw.rect(surface, (180, 180, 180), rect, 1)