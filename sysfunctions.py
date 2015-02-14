import pygame, sys
pygame.init()

def terminate():
	pygame.quit()
	sys.exit()

# Original function from pygame.org/wiki/toggle_fullscreen
def toggleFullScreen():
	screen = pygame.display.get_surface()
	tmp = screen.convert()
	caption = pygame.display.get_caption()
	cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
	w,h = screen.get_width(),screen.get_height()
	flags = screen.get_flags()
	bits = screen.get_bitsize()
    
	pygame.display.quit()
	pygame.display.init()
    
	screen = pygame.display.set_mode((w,h),flags^pygame.FULLSCREEN,bits)
	screen.blit(tmp,(0,0))
	pygame.display.set_caption("Breakout")
 
	pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
 
	pygame.mouse.set_visible(False)
    
	return screen
'''
def pause():
	pause = True
'''
