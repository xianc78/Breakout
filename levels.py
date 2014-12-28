import pygame, sys
import constants
pygame.init()
from brick import Brick

class level:
	layout = []
	brick_list = []

	def createLevel(self):
		# Set x and y coordinates to 0
		x = y = 0
		for line in self.layout.split():
			# Go through each line
			for brick in line:
				# Go through each character in each line and create a color brick or a space according to the character
                                if brick == "w":
                                        self.brick_list.append(Brick(x, y, constants.WHITE))
                                elif brick == "b":
                                        self.brick_list.append(Brick(x, y, constants.BLUE))
                                elif brick == "g":
                                        self.brick_list.append(Brick(x, y, constants.GREEN))
                                elif brick == "r":
                                        self.brick_list.append(Brick(x, y, constants.RED))
				elif brick == "_":
                                        pass
				else:
					print brick + " is not a valid character"
					raw_input("<press enter>")
					pygame.quit
					sys.exit()
                                x += 38 + constants.BRICK_MARGIN
			x = 0
			y += 13 + constants.BRICK_MARGIN

class level1(level):
	def __init__(self):
		self.layout = '''
		wwwwwwwwwwwwwwwwwww
		bbbbbbbbbbbbbbbbbbb
		ggggggggggggggggggg
		rrrrrrrrrrrrrrrrrrr
		'''
		self.createLevel()

class level2(level):
	def __init__(self):
		self.layout = '''
		_______wwwww_______
		__bbbbbbbbbbbbbbb__
		_ggggggggggggggggg_
		rrrrrrrrrrrrrrrrrrr
		 '''
		self.createLevel()

class level3(level):
        def __init__(self):
                self.layout = '''
                ________ww_________
                ____b_____b________
                _____g____g_gg_____
                __rrr--rr--rr______
                '''
                self.createLevel()

