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
		self.clock = pygame.time.Clock()
		self.running = True
		self.display = pygame.display.set_caption("Sapce War")
		self.all_sprite = pygame.sprite.Group()
		self.ship = ship.Ship()
		self.all_sprite.add(self.ship)
		for i in range(5):
			self.monster = monster.Monster()
			self.all_sprite.add(self.monster)

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
			self.screen.fill(self.white)
			self.all_sprite.draw(self.screen)

			#screen update
			pygame.display.update()
			self.all_sprite.update()

		pygame.quit()		
