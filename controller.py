import pygame
from src import ship
from src import monster 
class Controller:
	def __init__(self,width = 500,height=600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen =pygame.display.set_mode((self.width,self.height))
		self.fps = 60
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.clock = pygame.time.Clock()
		self.running = True
		self.display = pygame.display.set_caption("Space War")
		self.all_sprite = pygame.sprite.Group()
		self.ship = ship.Ship()
		self.all_sprite.add(self.ship)
		self.rocks = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.player = pygame.sprite.Group()  # create a new sprite group for ship for collsion 
		self.player.add(self.ship) # add in to group because we have to use a new group to create collsion in pygame.
		for i in range(5):
			self.monster = monster.Monster()
			self.all_sprite.add(self.monster)
			self.rocks.add(self.monster)
		#load image
		
	def mainLoop(self):
		pygame.init()
		while self.running:
			self.clock.tick(self.fps)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False 
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.all_sprite.add(self.ship.shoot())
						self.bullets.add(self.ship.shoot())
			
			self.all_sprite.update()
			hits = pygame.sprite.groupcollide(self.rocks,self.bullets,True,True)	
			for hit in hits:
				print("collsion happend")
				r = monster.Monster()
				self.all_sprite.add(r)
				self.rocks.add(r)
				
			
			
			hits = pygame.sprite.groupcollide(self.player,self.rocks,False,False)
			if hits:
				self.running = False 

			#screen update
			self.screen.fill(self.black)
			self.all_sprite.draw(self.screen)
			pygame.display.update()	



		pygame.quit()		
