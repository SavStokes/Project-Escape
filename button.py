import pygame
from pygame.locals import *

pygame.init()

# create screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set font
font = pygame.font.SysFont('Arial', 30)

# color hex codes
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 150, 255)

clicked = False

# create button class
class Button():
		
	# assign colors
	button_color = red
	hover_color = white
	click_color = blue
	text_color = black
	width = 180
	height = 70


	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text


	def create_button(self):
		
		global clicked
		action = False
			
		# get cursor position
		pos = pygame.mouse.get_pos()

		# button rectangle
		button = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
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

# put the button on the screen
final_button = Button(200, 200, 'BUTTON')

run = True
while run:

	screen.fill(yellow)

    # show that user clicked button
	if final_button.create_button():
		print('You clicked the button')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()