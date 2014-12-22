import pygame, sys, random
import constants
import levels
from pygame.locals import *
from paddle import Paddle
from ball import Ball
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
pygame.display.set_icon(pygame.Surface([32, 32]))

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

level_list = [levels.level1()]
levelno = 1
current_level = level_list[levelno - 1]

paddle = Paddle(pygame.mouse.get_pos()[0])
ball = Ball(random.randint(0, 800 - 10), random.randint(0, 600 - 10), current_level)
ball.paddle = paddle

def terminate():
	pygame.quit()
	sys.exit()

while True:
	pygame.display.set_caption("Breakout | Lives: " + str(paddle.lives))
	screen.fill(constants.BLACK)
	screen.blit(paddle.image, (paddle.rect.x, paddle.rect.y))
	screen.blit(ball.image, (ball.rect.x, ball.rect.y))
	for brick in current_level.brick_list:
		screen.blit(brick.image, (brick.rect.x, brick.rect.y))
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				terminate()
	paddle.update()
	ball.update()
	if len(current_level.brick_list) == 0:
		if levelno >= len(level_list):
			terminate()
		else:
			levelno += 1
			current_level = level_list[levelno]
			ball.level = current_level
	pygame.display.update()
	clock.tick(constants.FPS)
