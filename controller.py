import pygame
from src import ship
from src import monster 
from src import weapon
import json

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
		self.red = (255,0,0)
		self.black = (0,0,0)
		self.light_purple= (204,205,255)
		self.clock = pygame.time.Clock()
		self.running = True
		pygame.key.set_repeat(1, 50) #held keys will count as many key strikes

		self.display = pygame.display.set_caption("Save the Sea")

		self.font_name = pygame.font.match_font('arial')

	
		self.background_image = pygame.image.load("assets/ocean.png").convert()		
		self.show_init = True

	def mainLoop(self):

		"""																																																			
		This method checks to see whether or not the gameplay is continuing or if the gameplay is over. It accomplishes such by checking if the state of the game is either \u201crunning.\u201d If the game is in a \u201crunning\u201d state the gameplay of the program is run. 
		args: self which is the object that is created from the class. 
		return: none
		"""

		pygame.init()
		while self.running:
			if self.show_init: 
				self.draw_init()
				self.show_init = False
				self.all_sprite = pygame.sprite.Group()
				self.ship = ship.Ship("assets/jet (3).png")
				self.all_sprite.add(self.ship)
				self.rocks = pygame.sprite.Group()
				self.bullets = pygame.sprite.Group()
				self.player = pygame.sprite.Group()  # create a new sprite group for ship for collsion 
				self.player.add(self.ship) # add in to group because we have to use a new group to create collsion in pygame.
				self.score = 0
				self.health = self.ship.ship_health()	
				for i in range(12):
					self.monster = monster.Monster("assets/trash (2).png")
					self.all_sprite.add(self.monster)

					self.rocks.add(self.monster)
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False 

				elif event.type == pygame.KEYDOWN:
					
					keys = pygame.key.get_pressed() 			
					
					if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
						self.ship.move_right()
						self.weapon = weapon.Weapon(self.ship.shipx(),self.ship.shipy(),"assets/laser.png")
						self.all_sprite.add(self.weapon)
						self.bullets.add(self.weapon)
					elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
						self.ship.move_left()
						self.weapon = weapon.Weapon(self.ship.shipx(),self.ship.shipy(),"assets/laser.png")
						self.all_sprite.add(self.weapon)
						self.bullets.add(self.weapon)
					elif event.key == pygame.K_SPACE:
						self.weapon = weapon.Weapon(self.ship.shipx(),self.ship.shipy(),"assets/laser.png")
						self.all_sprite.add(self.weapon)
						self.bullets.add(self.weapon)
					elif (event.key == pygame.K_RIGHT):
						self.ship.move_right()
					elif (event.key == pygame.K_LEFT):
						self.ship.move_left()
					
			self.all_sprite.update()

			hits = pygame.sprite.groupcollide(self.bullets,self.rocks, True, True)
	
			if(hits):
				for hit in hits:					
					self.score += 10
					print(self.score)
					r = monster.Monster("assets/trash.png")
					self.all_sprite.add(r)
					self.rocks.add(r)
			
			phits = pygame.sprite.groupcollide(self.player,self.rocks,False,True)
			for phit in phits:
				self.health -= 30
				if self.health < 0:
					self.show_init = True
					self.endgame()
				

			#self.screen.fill(self.white)
			self.all_sprite.draw(self.screen)

			#screen update
			self.screen.blit(self.background_image, (0, 0))
			self.all_sprite.draw(self.screen)
			self.draw_text(self.screen, str(self.score), 18, 250, 10)
			self.draw_health(self.screen,self.health,10,10)
			pygame.display.update()	

		pygame.quit()		


	def draw_text(self, surf, text, size, x , y): 
	
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text,True,self.white)
		text_rect = text_surface.get_rect()
		text_rect.centerx = x
		text_rect.top = y
		surf.blit(text_surface,text_rect)

	def draw_init(self):
		pygame.init()
		self.screen.blit(self.background_image, (0, 0))
		self.draw_text(self.screen,'Save the Sea',64,250,150)

		self.draw_text(self.screen,'\u2190 \u2192: Control movement of ship. Use space to shoot the bullet',15,250,250)
		
		self.draw_text(self.screen,'Press any key to start the game ! ',15,250,350)
		pygame.display.update()
		waiting = True
		while waiting:
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

				elif event.type == pygame.KEYUP:
					waiting = False 
	
	def endgame(self):
		pygame.init()

		#fptr = open("etc/Scores.json", "r")

		#prev_scores = json.load(fptr)
		
		#print(prev_scores)
		#print(prev_scores["Highest Score"])


		#if prev_scores[0]["Highest Score"] < self.score: 
		#	fptr.close()
		#	fptr2 = open("etc/Scores.json", "w")
		#	
		#	prev_scores = self.score 
		#	fptr2.close()

		#else:
		#	fptr.close()
		#	fptr2 = open("etc/Scores.json", "w")
		#	prev_scores[] = self.score
		#	fptr2.close()

		self.screen.blit(self.background_image, (0, 0))
		self.draw_text(self.screen,'Game Over! ',75,250,150)
		self.draw_text(self.screen,'Your Score is: '+ f'{self.score}' ,50,250,250)
		
		self.draw_text(self.screen,'Press any key to restart the game ! ',15,250,350)
		pygame.display.update()
		waiting = True
		while waiting:
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

				elif event.type == pygame.KEYUP:
					waiting = False 
					
	def draw_health(self,surf,hp,x,y):
		if hp < 0:
			hp = 0
		bar_length = 100
		bar_height = 10
		fill = (hp/100)*bar_length
		outline_rect = pygame.Rect(x,y,bar_length,bar_height)
		fill_rect = pygame.Rect(x,y,fill,bar_height)
		pygame.draw.rect(surf,self.red,fill_rect)
		pygame.draw.rect(surf,self.light_purple,outline_rect,2)
