import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/tom-clancy-s-rainbow-6-game.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_wigth = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
target_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


running = True
while running:
    pass

pygame.quit()