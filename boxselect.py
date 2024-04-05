# import the pygame module
import pygame
pygame.init()

# set up the screen
# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BOX SELECTION")

font = pygame.font.SysFont("arialblack", 30)
text = (255, 255, 255)

def draw(text, font, color, x):
    display = font.render(text, True, (255, 255, 255))
    screen.blit(display, x)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # box 1
    box1 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(100, 150, 150, 150))
    draw(" B O X  1", font, text, box1)

    # box 2
    box2 = pygame.draw.rect(screen, (100, 0, 100), pygame.Rect(350, 150, 150, 150))
    draw(" B O X  2", font, text, box2)

    # box 3
    box3 = pygame.draw.rect(screen, (150, 0, 255), pygame.Rect(600, 150, 150, 150))
    draw(" B O X  3", font, text, box3)
    
    # title
    titlebox = pygame.draw.rect(screen, (255, 0, 10), pygame.Rect(25, 10, 750, 75))
    draw("     P L E A S E    S E L E C T    A    B O X ", font, text, titlebox)
    
    # play
    play = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(325, 400, 200, 50))
    draw(" P L A Y  -->", font, text, play)

    pygame.display.flip()
    