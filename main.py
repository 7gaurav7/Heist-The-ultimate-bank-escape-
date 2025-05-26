import pygame
import sys
from map import draw_map, BANK_MAP, TILE_SIZE
from player import Player

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heist: The Ultimate Bank Escape")
clock = pygame.time.Clock()

player = Player(1, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Background
    draw_map(screen)
    player.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(0, -1)
    elif keys[pygame.K_DOWN]:
        player.move(0, 1)
    elif keys[pygame.K_LEFT]:
        player.move(-1, 0)
    elif keys[pygame.K_RIGHT]:
        player.move(1, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
