import pygame

### will initialize the screen 
pygame.init()

### color format (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((800, 600))

### giving title to the scree
pygame.display.set_caption('Slither')




GameEvent = False
Game_x = 200
Game_y = 300
Game_x_change = 0

clock = pygame.time.Clock()

### looping all events
while not GameEvent:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameEvent = True

		### if an arrow key is pressed		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Game_x_change = -10
			if event.key == pygame.K_RIGHT:
				Game_x_change = 10	 

		### adding case if user lifts up from the key then movement stops 		
		#if event.type == pygame.KEYUP:
#			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#				Game_x_change = 0


	### will change according to last arrow key pressed			
	Game_x += Game_x_change 			
	GameDisplay.fill(white)	

	### parameter(ScreenObject, color, [x, y, w, h])
	pygame.draw.rect(GameDisplay, black, [Game_x, Game_y, 10, 100])

	### will update the whole display screen
	pygame.display.update()

	### give freeze time frame per seconds
	clock.tick(15)	


### quitting from pygame
pygame.quit()

### quitting from program
quit()