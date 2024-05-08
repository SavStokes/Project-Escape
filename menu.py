import pygame
import button
import random
from settings import *
from sprites import *

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BOX SELECTION")

# game variables
game_paused = False
menu_state = "boxes"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
text_color = (255, 255, 255)

# draw text
def draw_text(text, font, color, x, y):
  img = font.render(text, True, color)
  screen.blit(img, (x, y))

# load button images
# first screen
box1_img = pygame.image.load("one.png").convert_alpha()
box2_img = pygame.image.load("two.png").convert_alpha()
box3_img = pygame.image.load("three.png").convert_alpha()
# second screen
arrow_img = pygame.image.load('arrow.png').convert_alpha()
# third screen
nonogram_img = pygame.image.load('nonogram.png').convert_alpha()
worddle_img = pygame.image.load('worddle.png').convert_alpha()
slide_img = pygame.image.load('slide.png').convert_alpha()


# create button instances
# first screen
box1_button = button.Button(80, 250, box1_img, 1)
box2_button = button.Button(350, 250, box2_img, 1)
box3_button = button.Button(575, 250, box3_img, 1)
# second screen
arrow_button = button.Button(350, 400, arrow_img, 1)
# third screen
nonogram_button = button.Button(80, 250, nonogram_img, 1)
worddle_button = button.Button(350, 250, worddle_img, 1)
slide_button = button.Button(575, 250, slide_img, 1)

# game loop
run = True
while run:

  screen.fill((250, 160, 160))

  #check if game is paused
  if game_paused == True:
    # check menu state
    if menu_state == "boxes":
      font = pygame.font.SysFont("arialblack", 40)
      draw_text("PICK A BOX", font, text_color, 275, 100)
      font = pygame.font.SysFont("arialblack", 20)
      draw_text("BOX 1", font, text_color, 100, 220)
      draw_text("BOX 2", font, text_color, 375, 220)
      draw_text("BOX 3", font, text_color, 600, 220)
      # draw box buttons
      if box1_button.draw(screen):
        menu_state = "go"
      if box2_button.draw(screen):
        menu_state = "go"
      if box3_button.draw(screen):
        menu_state = "go"
    if menu_state == "go":
        font = pygame.font.SysFont("arialblack", 40)
        draw_text("YOU'VE PICKED A BOX!", font, text_color, 150, 200)
        draw_text("NOW LET'S PICK A PUZZLE", font, text_color, 100, 250)
        if arrow_button.draw(screen):
            menu_state = "puzzle"
    # check if the options menu is open
    if menu_state == "puzzle":
      pygame.display.set_caption("GAME SELECTION")
      font = pygame.font.SysFont("arialblack", 40)
      draw_text("PICK A PUZZLE", font, text_color, 250, 100)
      font = pygame.font.SysFont("arialblack", 20)
      draw_text("NONOGRAM PUZZLE", font, text_color, 40, 220)
      draw_text("WORDDLE PUZZLE", font, text_color, 300, 220)
      draw_text("SLIDING PUZZLE", font, text_color, 550, 220)
      #draw the different options buttons
      if nonogram_button.draw(screen):
        print("NONOGRAM PUZZLE")
        menu_state == "nonogram"
      if worddle_button.draw(screen):
        menu_state == "worddle"
        pygame.display.set_caption("WORDDLE")
        import worddle
      if slide_button.draw(screen):
        print("SLIDING PUZZLE")
        menu_state == "sliding"
  else:
    font = pygame.font.SysFont("arialblack", 40)
    draw_text("WELCOME TO PROJECT ESCAPE !", font, text_color, 25, 200)
    draw_text("Press SPACE to CONTINUE", font, text_color, 100, 250)


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()