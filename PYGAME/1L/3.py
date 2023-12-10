import pygame
import time
import random
from pygame import mixer

pygame.init()
display_width = 650
display_hight = 650
car_width = 50
car_height = 200
gameDisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
carIMG = pygame.image.load("car1.png")
carIMG = pygame.transform.scale(carIMG, (150, 180))
car2IMG = pygame.image.load("car2.png")
car2IMG = pygame.transform.scale(car2IMG,(140, 140))
coinIMG = pygame.image.load('coinnorm.png')
coinIMG = pygame.transform.scale(coinIMG, (50, 50))
roadIMG = pygame.image.load("road3.png")
roadIMG = pygame.transform.scale(roadIMG, (700, 700))


car_x = ((display_width)-(car_height))
car_y = ((display_hight)-(car_height))+50
car_x_change = 0
road_start_x = -50
road_end_x = display_width
thing_startx = random.randrange(road_start_x, road_end_x - car_width)
thing_starty = -600
coin_x = random.randrange(road_start_x, road_end_x - car_width)
coin_y =random.randrange(0 , 400)
coin_speed = 5
thing_speed = 5
thing_h = 40
thing_w = 40
count=0
gameExit = False
n = 10
def hightscore(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score :" + str(count), True, (0, 0, 0))
    gameDisplay.blit(text, (550, 30))

def draw_enemy(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))

def draw_coin(coin_x, coin_y, coinIMG):
    gameDisplay.blit(coinIMG, (coin_x, coin_y))

def car(x, y):
    gameDisplay.blit(carIMG, (x, y))

def crash(x, y):
    gameDisplay.blit(game_over, (x, y))
    pygame.display.update()
    time.sleep(2)

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit =True
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -10
            elif event.key == pygame.K_RIGHT:
                car_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_x_change = 0
    car_x+=car_x_change

    if car_x > road_end_x - 100:
        car_x = road_end_x - 100
    if car_x <road_start_x:
        car_x = road_start_x
        print(road_start_x,car_x)
    gameDisplay.blit(roadIMG, (0, 0))
    car(car_x, car_y)
    draw_enemy(thing_startx, thing_starty, car2IMG)
    draw_coin(coin_x, coin_y, coinIMG)
    hightscore(count)
    if car_y < thing_starty +thing_h + 70:
        if car_x >= thing_startx and car_x <= thing_startx + thing_w +10:
            game_over = pygame.image.load('game.png')
            game_over = pygame.transform.scale(game_over, (400,400))
            thing_startx = random.randrange(road_start_x, road_end_x - car_width)
            thing_starty = -600
            count = 0
            coin_x = random. randrange(road_start_x + 30, road_end_x - 150)
            coin_y = -500
            thing_speed = 7
            crash(160, 130)
        if car_x +car_width >= thing_startx and car_x +car_width <= thing_startx + thing_w:
            thing_startx = random.randrange(road_start_x, road_end_x -car_width)
            thing_starty = -600
            game_over = pygame.image.load('game.png')
            game_over = pygame.transform.scale(game_over, (400, 400))
            count = 0
            coin_x = random.randrange(road_start_x + 30, road_end_x -150)
            coin_y = -500
            thing_speed = 7
            crash(160, 130)
    coin_y +=coin_speed
    thing_starty += thing_speed
    coin_w = random.randrange(49, 50)
    coin_h = random.randrange(49, 50)
    if car_y < coin_y + coin_h /2:
        if car_x + car_width / 2 >= coin_x +coin_w /2 and car_x -car_width/2 <=coin_x + coin_w / 2:
            count+=1
            coinIMG = pygame.image.load('coinnorm.png')
            coinIMG = pygame.transform.scale(coinIMG, (coin_w, coin_h))
            coin_x = random.randrange(road_start_x + 30, road_end_x -150)
            coin_y = -500
        if car_x + car_width / 2 >= coin_x and car_x -car_width/2 <=coin_x + coin_w / 2:
            count+=1
            coinIMG = pygame.image.load('coinnorm.png')
            coinIMG = pygame.transform.scale(coinIMG, (coin_w, coin_h))
            coin_x = random.randrange(road_start_x + 30, road_end_x -150)
            coin_y = -500

    if count == n:
        thing_speed +=3
        n += 10



    if coin_y > display_hight:
        coin_x = random.randrange(road_start_x + 30, road_end_x - 150)
        coin_y = -500
    if thing_starty > display_hight:
        thing_startx = random.randrange(road_start_x + 30, road_end_x - 150)
        thing_starty = -500

    pygame.display.update()
    clock.tick(120)