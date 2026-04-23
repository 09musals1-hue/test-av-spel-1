import pygame
import random
import os
print(os.listdir())

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fågelspel")

WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
RED = (255, 0, 0)

# Ladda fågelbild
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (60, 60))  # ändra storlek

bird_x = 100
bird_y = 200
bird_speed = 5

# Mat
food_size = 20
food_x = random.randint(0, WIDTH - food_size)
food_y = random.randint(0, HEIGHT - food_size)

score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y -= bird_speed
    if keys[pygame.K_DOWN]:
        bird_y += bird_speed
    if keys[pygame.K_LEFT]:
        bird_x -= bird_speed
    if keys[pygame.K_RIGHT]:
        bird_x += bird_speed

    # Rita fågelbild istället för fyrkant
    screen.blit(bird_img, (bird_x, bird_y))

    # Rita mat
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))

    # Kollision (anpassad för bild)
    bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
    food_rect = pygame.Rect(food_x, food_y, food_size, food_size)

    if bird_rect.colliderect(food_rect):
        score += 1
        food_x = random.randint(0, WIDTH - food_size)
        food_y = random.randint(0, HEIGHT - food_size)

    score_text = font.render(f"Poäng: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
