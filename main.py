import pygame, sys, random, platform
import constants
import levels
import sysfunctions
import text
from pygame.locals import *
from paddle import Paddle
from ball import Ball
pygame.init()

# Creating the screen and setting the icon and title
if platform.system() == "Windows":
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), FULLSCREEN)
else:
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	pygame.display.toggle_fullscreen()
pygame.display.set_caption("Breakout")
pygame.display.set_icon(pygame.Surface([32, 32]))
sysfunctions.screen = screen

# Creating the clock
clock = pygame.time.Clock()

# Making the mouse cursor invisable
pygame.mouse.set_visible(False)

# Creating a list of levels and setting the current level
level_list = [levels.level1, levels.level2, levels.level3]
levelno = 1
current_level = level_list[levelno - 1]()

# Creating the paddle
paddle = Paddle(pygame.mouse.get_pos()[0])
paddle.screen = screen

# Creating the ball
ball = Ball(random.randint(0, 800 - 10), random.randint(0, 300 - 10), current_level)
ball.paddle = paddle

'''
# Quit game
def terminate():
	pygame.quit()
	sys.exit()
'''

paused = False
pauseText = text.pauseText()

nextLevel = text.nextLevelText()
LifeCounter = text.lifeCounter()

def titleScreen():
	titleText = text.titleText()
	enterText = text.enterText()
	while True:
		screen.blit(titleText.text, titleText.rect)
		screen.blit(enterText.text, enterText.rect)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return None
		pygame.display.update()

titleScreen()

# Game loop
while True:
	pygame.display.set_caption("Breakout | Lives: " + str(paddle.lives))
	screen.fill(constants.BLACK)
	screen.blit(LifeCounter.text, LifeCounter.rect)
	screen.blit(paddle.image, (paddle.rect.x, paddle.rect.y))
	screen.blit(ball.image, (ball.rect.x, ball.rect.y))
	for brick in current_level.brick_list:
		screen.blit(brick.image, (brick.rect.x, brick.rect.y))
	for event in pygame.event.get():
		if event.type == QUIT:
			sysfunctions.terminate()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				if platform.system() == "Windows":
					screen = sysfunctions.toggleFullScreen()
				else:
					pygame.display.toggle_fullscreen()
			elif event.key == K_p:
				paused = True
			'''
			# For debugging purposes
			elif event.key == K_F1:
				paddle.lives = 0
			'''	
	while paused:
		screen.blit(pauseText.text, pauseText.rect)
		for event in pygame.event.get():
			if event.type == QUIT:
				sysfunctions.terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					if platform.system() == "Windows":
						screen = sysfunctions.toggleFullScreen()
					else:
						pygame.display.toggle_fullscreen()
				elif event.key == K_p:
					paused = False
		pygame.display.update()

	paddle.update()
	ball.update()
	LifeCounter.text = text.fontObj.render("Live(s): " + str(paddle.lives), True, constants.WHITE)
	# If all the bricks are hit, go to next level or end the game
	if len(current_level.brick_list) == 0:
		levelno += 1
		if levelno > len(level_list):
			sysfunctions.terminate()
		else:
			screen.blit(nextLevel.text, nextLevel.rect)
			pygame.display.update()
			pygame.time.wait(500)
			current_level = level_list[levelno - 1]()
			ball.level = current_level
			ball.resetPosition()
	# Update the screen and clock
	pygame.display.update()
	clock.tick(constants.FPS)
