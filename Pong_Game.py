import pygame
import random
import sys


def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10, 100)
    ball_speed_x *= random.choice((-1, 1))
    ball_speed_y *= random.choice((-1, 1))


def point_won(winner):
    global cpu_points, player_points
    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points += 1
    reset_ball()


def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_hight or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        point_won("cpu")

    if ball.left <= 0:
        point_won('player')

    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1


def animate_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_hight:
        player.bottom = screen_hight


def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed

    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6

    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_hight:
        cpu.bottom = screen_hight


pygame.init()

screen_width = 1000
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Welcome Pong Game!")

clock = pygame.time.Clock()
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width/2, screen_hight/2)

cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = screen_hight/2

player = pygame.Rect(0, 0, 20, 100)
player.midright = (screen_width, screen_hight/2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6

cpu_points, player_points = 0, 0

score_font = pygame.font.Font(None, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0

    # Change the position of the game objects
    animate_ball()
    animate_player()
    animate_cpu()

    # Draw the game object Игровой объект
    screen.fill('black')

    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")

    screen.blit(cpu_score_surface, (screen_width/4, 20))
    screen.blit(player_score_surface, (3*screen_width / 4, 20))

    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_hight))
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.rect(screen, 'white', player)

    # Update the display обновление экрана
    pygame.display.update()
    clock.tick(60)
