# import the pygame module
import pygame
pygame.init()

# set up the screen
# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Selection")

#sets font size and color
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

    screen.fill((250, 250, 250))

    #game 1
    game1_default = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(262.5, 150, 307, 50))
    draw("  Game  1  Default", font, text, game1_default)
    
    game1_random = pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(262.5, 200, 307, 50))
    draw(" Game  1  Random", font, text, game1_random)

    game1_custom = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(262.5, 250, 307, 50))
    draw(" Game  1  Custom", font, text, game1_custom)

    #game 2
    game2_default = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(262.5, 300, 307, 50))
    draw("  Game  2  Default", font, text, game2_default)
    
    game2_random = pygame.draw.rect(screen, (0, 255, 150), pygame.Rect(262.5, 350, 307, 50))
    draw(" Game  2  Random", font, text, game2_random)

    game2_custom = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(262.5, 400, 307, 50))
    draw(" Game  2 Custom", font, text, game2_custom)

    #title
    game_selection = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 50, 425, 50))
    draw("        Game Selection ", font, text, game_selection)
    pygame.display.flip()

    