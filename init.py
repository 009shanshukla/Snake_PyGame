import pygame
import time

### will initialize the screen 
pygame.init()

### color format (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

DisplayWidth = 800
DisplayHeight = 600

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))

### giving title to the scree
pygame.display.set_caption('Slither')



### Game variables
GameExit = False
Game_x = DisplayWidth/2
Game_y = DisplayHeight/2
Game_x_change = 0
Game_y_change = 0
BlockSize = 10

### clock object initialization
clock = pygame.time.Clock()
FPS = 30

### font object initialization using system font
font = pygame.font.SysFont(None, 25)

### message that needs to be printed on screen
def message_to_screen(msg, color):
	ScreenText = font.render(msg, True, color)
	GameDisplay.blit(ScreenText, [DisplayWidth/2, DisplayHeight/2])

### looping all events
while not GameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameExit = True

		### if an arrow key is pressed		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Game_x_change = -BlockSize
				Game_y_change = 0
			elif event.key == pygame.K_RIGHT:
				Game_x_change = BlockSize
				Game_y_change = 0
			elif event.key == pygame.K_UP:
				Game_y_change = -BlockSize
				Game_x_change = 0
			elif event.key == pygame.K_DOWN:
				Game_y_change = BlockSize
				Game_x_change = 0

		### off the boundary			
		if Game_x >= DisplayWidth or Game_x < 0 or Game_y >= DisplayHeight or Game_y < 0:
			GameExit = True			 

		### adding case if user lifts up from the key then movement stops 		
		#if event.type == pygame.KEYUP:
#			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#				Game_x_change = 0


	### will change according to last arrow key pressed			
	Game_x += Game_x_change 
	Game_y += Game_y_change			
	GameDisplay.fill(white)	

	### parameter(ScreenObject, color, [x, y, w, h])
	pygame.draw.rect(GameDisplay, black, [Game_x, Game_y, BlockSize, BlockSize])

	### will update the whole display screen
	pygame.display.update()

	### give freeze time frame per seconds
	clock.tick(FPS)	

### final msg on screen for 2 secs
message_to_screen("You Lose", red)
pygame.display.update()
time.sleep(2)

### quitting from pygame
pygame.quit()

### quitting from program
quit()