import pygame

pygame.init()
#size of window
size = width, height = 600, 600
#colors
black = [0, 0, 0]
white = [255, 255, 255]

screen = pygame.display.set_mode(size)

while True:
    screen.fill(black)

    pygame.draw.rect(screen,white,pygame.Rect(10,30,60,60))
    pygame.display.flip()



