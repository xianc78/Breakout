import pygame
import constants

fontObj = pygame.font.SysFont("arial", 32)

class pauseText:
	def __init__(self):
		self.text = fontObj.render("Paused", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
