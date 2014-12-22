import pygame, sys
from pygame.locals import *
pygame.init()

class Brick:
	def __init__(self, x, y, color):
		self.image = pygame.Surface([40, 13])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
