import pygame, sys, random
import constants
pygame.init()

class Ball:
	def __init__(self, x, y, level, paddle = None):
		self.image = pygame.Surface([10, 10])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = -5
		self.change_y = 5
		self.level = level

	def update(self):
		self.rect.x += self.change_x
		if self.rect.x < 0 or self.rect.right > constants.SCREEN_WIDTH:
			self.change_x *= -1
		self.rect.y += self.change_y
		for brick in self.level.brick_list:
			if self.rect.colliderect(brick.rect):
				self.level.brick_list.remove(brick)
				#self.change_x *= -1
				self.change_y *= -1
				self.paddle.score += 1
		if self.rect.colliderect(self.paddle.rect):
			self.change_y *= -1
		if self.rect.y > constants.SCREEN_HEIGHT - self.rect.height:
			self.paddle.lives -= 1
			self.resetPosition()
		elif self.rect.top < 0:
			self.change_y *= -1

	def resetPosition(self):
		self.rect.x = random.randint(0, 790)
		self.rect.y = random.randint(0, 300)
