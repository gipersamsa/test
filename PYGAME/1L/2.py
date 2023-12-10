import pygame
import sys

FPS = 60
W = 1500
H = 700
WHITE = (255, 255, 255)
BLUE = (0, 0, 212)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = 1
y = 650
x2 = 50+300
y2 = 650
r = 50
x3 = 50
y3 = 550

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((190, 123, 12))
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.draw.circle(sc, BLUE, (x2, y2), r)
    pygame.draw.rect(sc, BLUE, (x3, y3, 300,100))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 5
        x2 -= 5
        x3 -=5
    elif keys[pygame.K_RIGHT]:
        x += 5
        x2 += 5
        x3 += 5
    elif keys[pygame.K_UP]:
        y -= 5
        
    elif keys[pygame.K_DOWN]:
        y += 5

    if(x>1450):
        x = 1450
    elif(x<50):
        x = 50
    elif(y>650):
        y=650
    elif(y<50):
        y=50

    clock.tick(FPS)