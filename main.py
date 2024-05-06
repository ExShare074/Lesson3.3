import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("image/tom.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("image/target.png")
target_wigth = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
target_speed = 10

score = 0 # счётчик очков

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_wigth and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()