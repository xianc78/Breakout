import pygame, sys
import constants
pygame.init()

class Paddle:
	def __init__(self, x):
		self.image = pygame.Surface([75, 10])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
		self.score = 0
		self.lives = 3

	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0]
		if self.rect.x > constants.SCREEN_WIDTH - self.rect.width:
			self.rect.x = constants.SCREEN_WIDTH - self.rect.width
		elif self.rect.x < 0:
			self.rect.x = 0
		if self.lives <= 0:
                        pygame.quit()
                        sys.exit()
