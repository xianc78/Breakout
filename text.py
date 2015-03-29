'''
Todo:
* make a parent class for all three objects
* make a life counter for fullscreen mode
'''
import pygame
import constants

fontObj = pygame.font.SysFont("arial", 32)
fontObjLarge = pygame.font.SysFont("arial", 48)

class textObj:
	text = None

class pauseText(textObj):
	def __init__(self):
		self.text = fontObj.render("Paused", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class gameOverText(textObj):
	def __init__(self):
		self.text = fontObj.render("Game Over", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class nextLevelText(textObj):
	def __init__(self):
		self.text = fontObj.render("Level Complete", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class lifeCounter(textObj):
	def __init__(self):
		self.text = fontObj.render("Live(s): ", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.bottomleft = (0, constants.SCREEN_HEIGHT)

class titleText(textObj):
	def __init__(self):
		self.text = fontObjLarge.render("Breakout", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
