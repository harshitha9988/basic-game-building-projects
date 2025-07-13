import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen with Elements")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('Arial', 36)

text_surface = font.render('Welcome to the Game!', True, BLUE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, pygame.Rect(300, 200, 200, 100))

    screen.blit(text_surface, (250, 100)) 

    pygame.display.flip()

pygame.quit()
sys.exit()