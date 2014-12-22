import pygame
import constants
pygame.init()
from brick import Brick

class level:
	layout = []
	brick_list = []

	def createLevel(self):
		x = y = 0
		for line in self.layout.split():
			for brick in line:
                                if brick == "w":
                                        self.brick_list.append(Brick(x, y, constants.WHITE))
                                elif brick == "b":
                                        self.brick_list.append(Brick(x, y, constants.BLUE))
                                elif brick == "g":
                                        self.brick_list.append(Brick(x, y, constants.GREEN))
                                elif brick == "r":
                                        self.brick_list.append(Brick(x, y, constants.RED))
                                else:
                                        pass
                                x += 38 + constants.BRICK_MARGIN
			x = 0
			y += 13 + constants.BRICK_MARGIN

class level1(level):
	def __init__(self):
		self.layout = '''
		wwwwwwwww
		bbbbbbbbb
		ggggggggg
		rrrrrrrrr
		'''
		x = y = 0
		self.createLevel()
