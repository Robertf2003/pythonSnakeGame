import pygame

pygame.init()
#size of window
size = width, height = 600, 600

blackRGB = [0, 0, 0]
whiteRGB = [255, 255, 255]

initialX = 300
initialY = 300
widthOfWormSquare = 30
screen = pygame.display.set_mode(size)
wormBlock = pygame.Rect(initialX, initialY, widthOfWormSquare, widthOfWormSquare)
while True:
    screen.fill(blackRGB)
    pygame.draw.rect(screen, whiteRGB, block)
    pygame.display.flip()



