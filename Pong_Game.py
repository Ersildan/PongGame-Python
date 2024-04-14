import sys
import pygame

pygame.init()

screen_width = 1200
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Welcome Pong Game!")

clock = pygame.time.Clock()
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width/2, screen_hight/2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw the game object
    pygame.draw.rect(screen, 'white', ball)

    #Update the display
    pygame.display.update()
    clock.tick(60)
