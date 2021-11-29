import pygame
from src import ship
class Controller:
	def __init__(self,width = 500,height=600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen =pygame.display.set_mode((self.width,self.height))
		self.fps = 60
		self.white = (255,255,255)
		self.clock = pygame.time.Clock()
		self.running = True
		self.display = pygame.display.set_caption("Sapce War")
		self.all_sprite = pygame.sprite.Group()
		self.ship = ship.Ship()
		self.all_sprite.add(self.ship)
	def mainLoop(self):
		pygame.init()
		while self.running:
			self.clock.tick(self.fps)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False 
			self.screen.fill(self.white)
			self.all_sprite.draw(self.screen)
			pygame.display.update()
		pygame.quit()		
