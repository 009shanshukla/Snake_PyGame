import pygame
import random

### will initialize the screen 
pygame.init()

### color format (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

DisplayWidth = 800
DisplayHeight = 600

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))

### giving title to the scree
pygame.display.set_caption('Slither')

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

### displaying snake on screen
def snake(BlockSize, SnakeList):
	for XnY in SnakeList:
		pygame.draw.rect(GameDisplay, green, [XnY[0], XnY[1], BlockSize, BlockSize])		

### looping all events
def GameLoop():
	### Game variables
	GameExit = False
	GameOver = False
	Game_x = DisplayWidth/2
	Game_y = DisplayHeight/2
	Game_x_change = 0
	Game_y_change = 0

	### snake list will contain head list and rest body list 
	SnakeList = []
	SnakeLength = 1

	### snake's co-ordinate will be always multiple of 10, so do apple's. hence rounding number to its lowest multiple of 10
	RandAppleX = round(random.randrange(0, DisplayWidth - BlockSize)/10.0)*10.0
	RandAppleY = round(random.randrange(0, DisplayHeight- BlockSize)/10.0)*10.0
	
	while not GameExit:

		### if game is over
		while GameOver == True:
			GameDisplay.fill(white)
			message_to_screen("You Loose, Press c to continue or q to quit", red)
			pygame.display.update()

			### if c ,q our quit is pressed	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					GameExit = True
					GameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						GameExit = True
						GameOver = False
					if event.key == pygame.K_c:
						GameLoop()		

		### if one of arrow keys or quit is pressed				
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
			GameOver = True			 

		### will change according to last arrow key pressed			
		Game_x += Game_x_change 
		Game_y += Game_y_change			
		GameDisplay.fill(white)

		### fitting apple's location 	
		pygame.draw.rect(GameDisplay, red, [RandAppleX, RandAppleY, BlockSize, BlockSize])


		
		SnakeHead = []
		SnakeHead.append(Game_x)
		SnakeHead.append(Game_y)
		SnakeList.append(SnakeHead)

		if len(SnakeList) > SnakeLength:
			del SnakeList[0]

		snake(BlockSize, SnakeList)
		
		### will update the whole display screen
		pygame.display.update()

		### apple's eaten condition
		if Game_x == RandAppleX and Game_y == RandAppleY:
			RandAppleX = round(random.randrange(0, DisplayWidth - BlockSize)/10.0)*10.0
			RandAppleY = round(random.randrange(0, DisplayHeight- BlockSize)/10.0)*10.0

		### give freeze time frame per seconds
		clock.tick(FPS)	

	### quitting from pygame
	pygame.quit()

	### quitting from program
	quit()
GameLoop()	
