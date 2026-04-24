import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fågelspel")

WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
BIRD_COLOR = (255, 255, 0)

bird_img = None
bird_image_path = "bird.png"
if os.path.isfile(bird_image_path):
    bird_img = pygame.image.load(bird_image_path)
elif os.path.isdir(bird_image_path):
    supported = [f for f in os.listdir(bird_image_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"))]
    if supported:
        bird_img = pygame.image.load(os.path.join(bird_image_path, supported[0]))
        print(f"Loaded bird image from {bird_image_path}/{supported[0]}")
    else:
        print(f"Hittade ingen bild i mappen {bird_image_path}")
else:
    print(f"Hittade ingen fil eller mapp {bird_image_path}, ritar en cirkel istället")

if bird_img:
    bird_img = pygame.transform.scale(bird_img, (60, 60))

bird_x = 200
bird_y = 300
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

    # Gränser så fågeln inte går utanför skärmen
    bird_x = max(0, min(bird_x, WIDTH - 60))
    bird_y = max(0, min(bird_y, HEIGHT - 60))

    # Rita fågeln
    if bird_img:
        screen.blit(bird_img, (bird_x, bird_y))
        bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
    else:
        pygame.draw.circle(screen, BIRD_COLOR, (bird_x + 30, bird_y + 30), 30)
        bird_rect = pygame.Rect(bird_x, bird_y, 60, 60)

    # Rita mat
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))

    # Kollision
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
