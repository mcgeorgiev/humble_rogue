# move classes into other files

try:
	import pygame
	import sys
	import random
	from pygame.locals import *
except error as e:
	print e

pygame.init()

FPS = 30
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE =(255, 255, 255)

TILES_ACROSS = 20
TILES_DOWN = 15
TILE_SIZE = 32
SCREEN_WIDTH = TILES_ACROSS * TILE_SIZE
SCREEN_HEIGHT = TILES_DOWN * TILE_SIZE

class Map(object):
	def __init__(self):
		self.treasure = Treasure()
		self.map = []
		for i in range(TILES_ACROSS):
			row = []
			for j in range(TILES_DOWN):
				if self.treasure.position[0] == i and self.treasure.position[1] == j:
					row.append('T')
				else:
					row.append(0)
			self.map.append(row)

	def print_ascii_map(self):
		for row in self.map:
			print row



class Treasure(object):
	def __init__(self):
		self.position = (random.randint(1, TILES_ACROSS), random.randint(1, TILES_DOWN))
		self.image = pygame.image.load('images/chest.png')


class Game(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.player = pygame.image.load('images/grey1.png')
		self.clock = pygame.time.Clock()
		self.position = (0, 0)
		self.treasure = Treasure()
		self.map = Map()
		self.run()

	def draw_darkness(self):
		print self.map.map.__len__()
		for row in range(TILES_ACROSS):
			for col in range(TILES_DOWN):
				if self.map.map[row][col] == 0:
					pygame.draw.rect(self.screen, WHITE,
						(row*TILE_SIZE, col*TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))

	def draw_objects(self):
		for row in range(TILES_DOWN):
			for col in range(TILES_DOWN):
				if self.map.map[row][col] == 'T':
					self.screen.blit(self.map.treasure.image, (row*TILE_SIZE, col*TILE_SIZE))

	def move(self, hor, vert):
		x, y = self.position
		x += hor
		y += vert
		self.position = (x, y)
		self.draw_objects()
		self.draw_darkness()
		self.screen.blit(self.player, self.position)
		pygame.display.update()

	def run(self):
		while True:
			self.clock.tick(30)
			hor = 0
			vert = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT:
						hor = TILE_SIZE
					elif event.key == K_LEFT:
						hor = -TILE_SIZE
					elif event.key == K_UP:
						vert = -TILE_SIZE
					elif event.key == K_DOWN:
						vert = TILE_SIZE
				self.move(hor, vert)
				self.map.print_ascii_map()


def main():
	while True:
		game = Game()


if __name__ == "__main__":
	main()

































