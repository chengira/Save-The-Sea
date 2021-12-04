import pygame
from src import ship
from src import monster 

class Controller:

	def __init__(self,width = 500,height=600):

		"""
		This method sets all of the necessary parameters for the game window and game objects and spawns in all of the necessary objects for the game. It takes in parameters for the size of the window that the game runs in, creates said window, spawns in the  
		args: self which is the object created from the class. width (int) which is the width of the screen that the game is to be played on. height (int) which is the height of the screen that the game is to be played on. 
		return: none
		"""

		pygame.init()
		self.width = width
		self.height = height
		self.screen =pygame.display.set_mode((self.width,self.height))
		self.fps = 60
		self.white = (255,255,255)
		self.black = (0,0,0)
		self.clock = pygame.time.Clock()
		self.running = True
		self.display = pygame.display.set_caption("Save the Sea")
		self.all_sprite = pygame.sprite.Group()
		self.ship = ship.Ship("assets/airplane_1.0.png")
		self.all_sprite.add(self.ship)
		self.rocks = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.player = pygame.sprite.Group()  # create a new sprite group for ship for collsion 
		self.player.add(self.ship) # add in to group because we have to use a new group to create collsion in pygame.
		for i in range(5):
			self.monster = monster.Monster("assets/Seamonster_4.png")
			self.all_sprite.add(self.monster)

			self.rocks.add(self.monster)
		#load image
		


	def mainLoop(self):

		"""																																																			
		This method checks to see whether or not the gameplay is continuing or if the gameplay is over. It accomplishes such by checking if the state of the game is either “running.” If the game is in a “running” state the gameplay of the program is run. 
		args: self which is the object that is created from the class. 
		return: none
		"""

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

			hits = pygame.sprite.groupcollide(self.bullets,self.rocks, True, True)
	
			if(hits):
				for hit in hits:
					
					print("collsion happened")
					r = monster.Monster("assets/Seamonster_4.png")
					self.all_sprite.add(r)
					self.rocks.add(r)
			
			phits = pygame.sprite.groupcollide(self.player,self.rocks,False,False)
			if phits:
				self.running = False 

			#self.screen.fill(self.white)
			self.all_sprite.draw(self.screen)

			#screen update
			self.screen.fill(self.black)
			self.all_sprite.draw(self.screen)
			pygame.display.update()	

		pygame.quit()		
