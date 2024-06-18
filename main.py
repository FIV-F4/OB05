import pygame
import time
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (50, 50))
image_rect = image.get_rect()

image2 = pygame.image.load("image.png")
image2 = pygame.transform.scale(image2, (50, 50))
image_rect2 = image2.get_rect()

speed = 1

run = True
a,b,c = 255,255,255

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 25
            image_rect.y = mouseY - 25
    if image_rect.colliderect(image_rect2):
        print("collide")
        time.sleep(1)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

    screen.fill((a, b, c))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()
