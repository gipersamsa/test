import pygame
import sys

FPS = 60
bg_color = (189, 182, 162)

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
screen.fill(bg_color)

pygame.draw.rect(screen, (139, 69, 19), (1, 200, 400, 800))
pygame.draw.rect(screen, (0, 0, 212), (30, 350, 100, 100))
pygame.draw.rect(screen, (0, 0, 212), (270, 350, 100, 100))
pygame.draw.rect(screen, (0, 0, 0), (145, 450, 100, 150))
pygame.draw.polygon(screen, (0, 0, 0), ())

pygame.display.update()

while True:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()