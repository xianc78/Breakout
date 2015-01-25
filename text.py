'''
Todo:
* make a parent class for all three objects
* make a live counter for fullscreen mode
'''
import pygame
import constants

fontObj = pygame.font.SysFont("arial", 32)

class pauseText:
	def __init__(self):
		self.text = fontObj.render("Paused", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class gameOverText:
	def __init__(self):
		self.text = fontObj.render("Game Over", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class nextLevelText:
	def __init__(self):
		self.text = fontObj.render("Level Complete", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
