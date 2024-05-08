import pygame
from pygame.locals import *

pygame.init()


BLACK = (0,0,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
WHITE = (255,255,255)

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Nonogram Puzzle")

font = pygame.font.SysFont('Arial', 16)
text = WHITE

clicked = False
"""
class Button():
    button_color = WHITE
    hover_color = MAGENTA
    click_color = CYAN
    text_color = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def create_button(self):

        global clicked
        action = False

        pos = pygame.mouse.get_pos()
        
        button = Rect(self.x, self.y, self.width, self.height)

        if button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_color, button)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button)
        else:
            pygame.draw.rect(screen, self.button_color, button)

		# add text
        text_image = font.render(self.text, True, self.text_color)
        text_len = text_image.get_width()
        screen.blit(text_image, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action
"""
def draw(text, font, color, x):
    display = font.render(text, True, (255, 255, 255))
    screen.blit(display, x)
"""
box1 = Button(200,200, ' ')
"""
running = True
while running:
    '''
    if box1.create_button():
            print('You')'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BLACK)

    # tiny boxes
    box1_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 20, 20, 20))
    box1_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 45, 20, 20))
    box1_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 70, 20, 20))
    box1_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 95, 20, 20))
    box1_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 120, 20, 20))
    box1_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 145, 20, 20))
    box1_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 170, 20, 20))
    box1_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 195, 20, 20))
    box1_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 220, 20, 20))
    box1_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 245, 20, 20))
    box1_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 270, 20, 20))
    box1_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 295, 20, 20))
    box1_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 320, 20, 20))
    box1_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 345, 20, 20))
    box1_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 370, 20, 20))

    box2_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 20, 20, 20))
    box2_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 45, 20, 20))
    box2_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 70, 20, 20))
    box2_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 95, 20, 20))
    box2_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 120, 20, 20))
    box2_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 145, 20, 20))
    box2_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 170, 20, 20))
    box2_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 195, 20, 20))
    box2_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 220, 20, 20))
    box2_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 245, 20, 20))
    box2_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 270, 20, 20))
    box2_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 295, 20, 20))
    box2_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 320, 20, 20))
    box2_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 345, 20, 20))
    box2_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(125, 370, 20, 20)) 

    box3_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 20, 20, 20))
    box3_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 45, 20, 20))
    box3_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 70, 20, 20))
    box3_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 95, 20, 20))
    box3_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 120, 20, 20))
    box3_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 145, 20, 20))
    box3_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 170, 20, 20))
    box3_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 195, 20, 20))
    box3_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 220, 20, 20))
    box3_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 245, 20, 20))
    box3_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 270, 20, 20))
    box3_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 295, 20, 20))
    box3_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 320, 20, 20))
    box3_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 345, 20, 20))
    box3_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(150, 370, 20, 20))

    box4_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 20, 20, 20))
    box4_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 45, 20, 20))
    box4_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 70, 20, 20))
    box4_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 95, 20, 20))
    box4_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 120, 20, 20))
    box4_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 145, 20, 20))
    box4_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 170, 20, 20))
    box4_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 195, 20, 20))
    box4_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 220, 20, 20))
    box4_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 245, 20, 20))
    box4_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 270, 20, 20))
    box4_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 295, 20, 20))
    box4_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 320, 20, 20))
    box4_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 345, 20, 20))
    box4_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(175, 370, 20, 20)) 

    box5_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 20, 20, 20))
    box5_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 45, 20, 20))
    box5_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 70, 20, 20))
    box5_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 95, 20, 20))
    box5_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 120, 20, 20))
    box5_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 145, 20, 20))
    box5_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 170, 20, 20))
    box5_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 195, 20, 20))
    box5_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 220, 20, 20))
    box5_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 245, 20, 20))
    box5_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 270, 20, 20))
    box5_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 295, 20, 20))
    box5_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 320, 20, 20))
    box5_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 345, 20, 20))
    box5_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(200, 370, 20, 20))

    box6_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 20, 20, 20))
    box6_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 45, 20, 20))
    box6_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 70, 20, 20))
    box6_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 95, 20, 20))
    box6_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 120, 20, 20))
    box6_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 145, 20, 20))
    box6_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 170, 20, 20))
    box6_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 195, 20, 20))
    box6_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 220, 20, 20))
    box6_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 245, 20, 20))
    box6_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 270, 20, 20))
    box6_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 295, 20, 20))
    box6_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 320, 20, 20))
    box6_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 345, 20, 20))
    box6_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(225, 370, 20, 20)) 

    box7_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 20, 20, 20))
    box7_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 45, 20, 20))
    box7_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 70, 20, 20))
    box7_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 95, 20, 20))
    box7_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 120, 20, 20))
    box7_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 145, 20, 20))
    box7_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 170, 20, 20))
    box7_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 195, 20, 20))
    box7_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 220, 20, 20))
    box7_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 245, 20, 20))
    box7_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 270, 20, 20))
    box7_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 295, 20, 20))
    box7_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 320, 20, 20))
    box7_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 345, 20, 20))
    box7_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(250, 370, 20, 20))

    box8_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 20, 20, 20))
    box8_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 45, 20, 20))
    box8_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 70, 20, 20))
    box8_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 95, 20, 20))
    box8_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 120, 20, 20))
    box8_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 145, 20, 20))
    box8_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 170, 20, 20))
    box8_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 195, 20, 20))
    box8_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 220, 20, 20))
    box8_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 245, 20, 20))
    box8_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 270, 20, 20))
    box8_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 295, 20, 20))
    box8_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 320, 20, 20))
    box8_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 345, 20, 20))
    box8_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(275, 370, 20, 20)) 
        
    box9_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 20, 20, 20))
    box9_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 45, 20, 20))
    box9_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 70, 20, 20))
    box9_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 95, 20, 20))
    box9_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 120, 20, 20))
    box9_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 145, 20, 20))
    box9_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 170, 20, 20))
    box9_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 195, 20, 20))
    box9_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 220, 20, 20))
    box9_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 245, 20, 20))
    box9_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 270, 20, 20))
    box9_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 295, 20, 20))
    box9_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 320, 20, 20))
    box9_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 345, 20, 20))
    box10_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(300, 370, 20, 20))

    box10_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 20, 20, 20))
    box10_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 45, 20, 20))
    box10_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 70, 20, 20))
    box10_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 95, 20, 20))
    box10_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 120, 20, 20))
    box10_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 145, 20, 20))
    box10_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 170, 20, 20))
    box10_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 195, 20, 20))
    box10_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 220, 20, 20))
    box10_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 245, 20, 20))
    box10_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 270, 20, 20))
    box10_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 295, 20, 20))
    box10_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 320, 20, 20))
    box10_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 345, 20, 20))
    box10_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(325, 370, 20, 20)) 

    box11_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 20, 20, 20))
    box11_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 45, 20, 20))
    box11_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 70, 20, 20))
    box11_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 95, 20, 20))
    box11_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 120, 20, 20))
    box11_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 145, 20, 20))
    box11_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 170, 20, 20))
    box11_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 195, 20, 20))
    box11_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 220, 20, 20))
    box11_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 245, 20, 20))
    box11_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 270, 20, 20))
    box11_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 295, 20, 20))
    box11_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 320, 20, 20))
    box11_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 345, 20, 20))
    box11_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(350, 370, 20, 20))

    box12_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 20, 20, 20))
    box12_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 45, 20, 20))
    box12_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 70, 20, 20))
    box12_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 95, 20, 20))
    box12_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 120, 20, 20))
    box12_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 145, 20, 20))
    box12_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 170, 20, 20))
    box12_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 195, 20, 20))
    box12_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 220, 20, 20))
    box12_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 245, 20, 20))
    box12_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 270, 20, 20))
    box12_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 295, 20, 20))
    box12_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 320, 20, 20))
    box12_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 345, 20, 20))
    box12_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(375, 370, 20, 20)) 

    box13_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 20, 20, 20))
    box13_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 45, 20, 20))
    box13_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 70, 20, 20))
    box13_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 95, 20, 20))
    box13_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 120, 20, 20))
    box13_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 145, 20, 20))
    box13_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 170, 20, 20))
    box13_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 195, 20, 20))
    box13_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 220, 20, 20))
    box13_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 245, 20, 20))
    box13_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 270, 20, 20))
    box13_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 295, 20, 20))
    box13_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 320, 20, 20))
    box13_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 345, 20, 20))
    box13_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(400, 370, 20, 20))

    box14_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 20, 20, 20))
    box14_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 45, 20, 20))
    box14_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 70, 20, 20))
    box14_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 95, 20, 20))
    box14_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 120, 20, 20))
    box14_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 145, 20, 20))
    box14_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 170, 20, 20))
    box14_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 195, 20, 20))
    box14_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 220, 20, 20))
    box14_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 245, 20, 20))
    box14_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 270, 20, 20))
    box14_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 295, 20, 20))
    box14_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 320, 20, 20))
    box14_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 345, 20, 20))
    box14_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(425, 370, 20, 20)) 

    box15_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 20, 20, 20))
    box15_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 45, 20, 20))
    box15_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 70, 20, 20))
    box15_4 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 95, 20, 20))
    box15_5 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 120, 20, 20))
    box15_6 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 145, 20, 20))
    box15_7 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 170, 20, 20))
    box15_8 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 195, 20, 20))
    box15_9 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 220, 20, 20))
    box15_10 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 245, 20, 20))
    box15_11 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 270, 20, 20))
    box15_12 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 295, 20, 20))
    box15_13 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 320, 20, 20))
    box15_14 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 345, 20, 20))
    box15_15 = pygame.draw.rect(screen, WHITE, pygame.Rect(450, 370, 20, 20))
    
    # hint boxes
    hint1 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 20, 60, 20))
    draw("   hint 1", font, text, hint1)
    hint2 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 45, 60, 20))
    draw("   hint 2", font, text, hint2)
    hint3 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 70, 60, 20))
    draw("   hint 3", font, text, hint3)
    hint4 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 95, 60, 20))
    draw("   hint 4", font, text, hint4)
    hint5 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 120, 60, 20))
    draw("   hint 5", font, text, hint5)
    hint6 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 145, 60, 20))
    draw("   hint 6", font, text, hint6)
    hint7 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 170, 60, 20))
    draw("   hint 7", font, text, hint7)
    hint8 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 195, 60, 20))
    draw("   hint 8", font, text, hint8)
    hint9 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 220, 60, 20))
    draw("   hint 9", font, text, hint9)
    hint10 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 245, 60, 20))
    draw("  hint 10", font, text, hint10)
    hint11 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 270, 60, 20))
    draw("  hint 11", font, text, hint11)
    hint12 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 295, 60, 20))
    draw("  hint 12", font, text, hint12)
    hint13 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 320, 60, 20))
    draw("  hint 13", font, text, hint13)
    hint14 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 345, 60, 20))
    draw("  hint 14", font, text, hint14)
    hint15 = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(20, 370, 60, 20))
    draw("  hint 15", font, text, hint15)

    a = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(100, 400, 20, 60))
    draw("a", font, text, a)
    b = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(125, 400, 20, 60))
    draw("b", font, text, b)
    c = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(150, 400, 20, 60))
    draw("c", font, text, c)
    d = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(175, 400, 20, 60))
    draw("d", font, text, d)
    e = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(200, 400, 20, 60))
    draw("e", font, text, e)
    f = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(225, 400, 20, 60))
    draw("f", font, text, f)
    g = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(250, 400, 20, 60))
    draw("g", font, text, g)
    h = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(275, 400, 20, 60))
    draw("h", font, text, h)
    i = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(300, 400, 20, 60))
    draw("i", font, text, i)
    j = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(325, 400, 20, 60))
    draw("j", font, text, j)
    k = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(350, 400, 20, 60))
    draw("k", font, text, k)
    l = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(375, 400, 20, 60))
    draw("l", font, text, l)
    m = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(400, 400, 20, 60))
    draw("m", font, text, m)
    n = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(425, 400, 20, 60))
    draw("n", font, text, n)
    o = pygame.draw.rect(screen, (175, 0, 175), pygame.Rect(450, 400, 20, 60))
    draw("o", font, text, o)
    pygame.display.flip()
    

