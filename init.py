import pygame
import random

### will initialize the screen 
pygame.init()

### color format (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 155, 0)

DisplayWidth = 800
DisplayHeight = 600

### will contain direction of head
direction = "right"

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))

### giving title to the scree
pygame.display.set_caption('Slither')

### load image of icon, sanke head and apple
icon = pygame.image.load('apple1.jpg')
pygame.display.set_icon(icon)

img = pygame.image.load('snakeHead.jpg')
appleimg = pygame.image.load('apple1.jpg')
snakebody = pygame.image.load('Body.jpg')

### size of one unit of snake body and apple thickness
BlockSize = 20
AppleThickness = 30

### clock object initialization
clock = pygame.time.Clock()
FPS = 20    ## frame per second

### font object initialization using system font
SmallFont = pygame.font.SysFont("comicsansms", 25)
MedFont = pygame.font.SysFont("comicsansms", 50)
LargeFont = pygame.font.SysFont("comicsansms", 80)


### opening screen of game
def GameIntro():
	intro = True

	while intro:

		### events(Press c to enter or q to exit) and direct exit x 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					intro = False		

		GameDisplay.fill(white)
		message_to_screen("WELCOME TO SNAKE PYGAME", red, -100, "medium")
		message_to_screen("Help snake to eat apples ", black, -60)
		message_to_screen("The more snake eat, the more it will get longer ", black, -20)
		message_to_screen("If snake will run into itself or edges, snake will die", black, 20)
		message_to_screen("Press c to enter, Press p to pause or q to exit", blue, 100)
		pygame.display.update()
		clock.tick(15)


### function is used to get surface and inside rectangle of the whole text
def text_objects(text, color, FontSize):
	if FontSize == "small":
		TextSurface = SmallFont.render(text, True, color)
	elif FontSize == "medium":
		TextSurface = MedFont.render(text, True, color)
	elif FontSize == "large":
		TextSurface = LargeFont.render(text, True, color)		
	return TextSurface, TextSurface.get_rect()

### message that needs to be printed on screen
def message_to_screen(msg, color, y_displace = 0, FontSize = "small"):
	TextSurface, TextRect = text_objects(msg, color, FontSize)
	TextRect.center = (DisplayWidth/2), (DisplayHeight/2) + y_displace         ### y_dispalce is used to get y displacement from centre
	GameDisplay.blit(TextSurface, TextRect)

### displaying snake on screen
def snake(BlockSize, SnakeList):

	### change the direction of head image as per movement
	if direction == "right":
		head = img
		sbody = pygame.transform.rotate(snakebody, 180)
	if direction == "left":
		head = pygame.transform.rotate(img, 180)
		sbody = pygame.transform.rotate(snakebody, 180)
	if direction == "up":
		head = pygame.transform.rotate(img, 90)
		sbody = snakebody
	if direction == "down":
		head = pygame.transform.rotate(img,270)	
		sbody = snakebody		

	### first display the head which is  the last tuple of list	
	GameDisplay.blit(head, (SnakeList[-1][0], SnakeList[-1][1]))

	### then display the whole body
	for XnY in SnakeList[:-1]:
		GameDisplay.blit(sbody, (XnY[0], XnY[1]))

### random apple generation
def AppleLocGen():
	
	### snake's co-ordinate will be always multiple of 10, so do apple's. hence rounding number to its lowest multiple of 10
	RandAppleX = round(random.randrange(0, DisplayWidth - AppleThickness))#/10.0)*10.0
	RandAppleY = round(random.randrange(0, DisplayHeight- AppleThickness))#/10.0)*10.0
	return RandAppleX, RandAppleY

### score printing
def score(score):
	text = SmallFont.render("Score: "+ str(score), True, black)
	GameDisplay.blit(text, [0, 0])
					
### pausing the screen
def pause():
	paused = True
	message_to_screen("Paused", red, -100, "large")
	message_to_screen("Press c to continue or q to quit", black, -20)

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					paused = False

		pygame.display.update()					



### looping all events
def GameLoop():
	### Game variables
	global direction            ### by making global we can change it
	GameExit = False
	GameOver = False
	Game_x = DisplayWidth/2      ## Top left of Snake body
	Game_y = DisplayHeight/2
	Game_x_change = 10
	Game_y_change = 0

	### snake list will contain head list and rest body list 
	SnakeList = []
	SnakeLength = 1

	RandAppleX, RandAppleY = AppleLocGen()	
	
	while GameExit != True:
		if GameOver == True:
			message_to_screen("You Loose", red, -50,
							  FontSize="medium")  ### -50 is telling y-displacement from the centre of text
			message_to_screen("Press c to continue or q to quit", black, 50, FontSize="small")
			pygame.display.update()
                
		while GameOver == True:
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
					direction = "left"
					Game_x_change = -BlockSize
					Game_y_change = 0
				elif event.key == pygame.K_RIGHT:
					direction = "right"
					Game_x_change = BlockSize
					Game_y_change = 0
				elif event.key == pygame.K_UP:
					direction = "up"
					Game_y_change = -BlockSize
					Game_x_change = 0
				elif event.key == pygame.K_DOWN:
					direction = "down"
					Game_y_change = BlockSize
					Game_x_change = 0
				elif event.key == pygame.K_p:
					pause()	

		### off the boundary			
		if Game_x >= DisplayWidth or Game_x < 0 or Game_y >= DisplayHeight or Game_y < 0:
			GameOver = True			 

		### will change according to last arrow key pressed			
		Game_x += Game_x_change 
		Game_y += Game_y_change			
		GameDisplay.fill(white)

		### displaying apple image
		GameDisplay.blit(appleimg, (RandAppleX, RandAppleY))

		
		SnakeHead = []
		SnakeHead.append(Game_x)
		SnakeHead.append(Game_y)
		SnakeList.append(SnakeHead)


		### Note - Last element of the list will be the head of Snake 

		if len(SnakeList) > SnakeLength:
			del SnakeList[0]

		snake(BlockSize, SnakeList)

		### if in case any snake segment in the last except last one(which will be head) is head then it means collision
		for SnakeSegment in SnakeList[:-1]:
			if SnakeSegment == SnakeHead:
				GameOver = True
		
		score(SnakeLength - 1)
		### will update the whole display screen
		pygame.display.update()

 
		if Game_x > RandAppleX and Game_x < RandAppleX + AppleThickness or Game_x + BlockSize > RandAppleX and Game_x + BlockSize < RandAppleX + AppleThickness:
			if Game_y > RandAppleY and Game_y < RandAppleY + AppleThickness:
				RandAppleX, RandAppleY = AppleLocGen()	
				SnakeLength += 1	
			elif Game_y + BlockSize > RandAppleY and Game_y + BlockSize < RandAppleY + AppleThickness:
				RandAppleX, RandAppleY = AppleLocGen()	
				SnakeLength += 1			    
		
		### give freeze time frame per seconds
		clock.tick(FPS)	

	### quitting from pygame
	pygame.quit()

	### quitting from program
	quit()

GameIntro()	
GameLoop()	
