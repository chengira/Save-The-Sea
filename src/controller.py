import pygame
from src import ship
from src import monster 
from src import weapon
import json

class Controller:

	def __init__(self,width = 500,height=600):

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
		pygame.key.set_repeat(1, 75) #held keys will count as many key strikes

		self.display = pygame.display.set_caption("Save the Sea")

		self.font_name = pygame.font.match_font('arial')

	
		self.background_image = pygame.image.load("assets/ocean.png").convert()		
		self.show_init = True

		self.kill_counter = 0

	def mainLoop(self):

		"""																																																			
		This method checks to see whether or not the gameplay is continuing or if the gameplay is over. It accomplishes such by checking if the state of the game is running. If the game is in a running state the gameplay of the program is ran. 
		args: none 
		return: none
		"""

		pygame.init()
		while self.running:
			if self.show_init: 
				self.start_loop()
				self.show_init = False
				self.all_sprite = pygame.sprite.Group()
				self.ship = ship.Ship("assets/jet (3).png")
				self.all_sprite.add(self.ship)
				self.trash = pygame.sprite.Group()
				self.bullets = pygame.sprite.Group()
				self.player = pygame.sprite.Group()  # create a new sprite group for ship for collsion 
				self.player.add(self.ship) # add in to group because we have to use a new group to create collsion in pygame.
				self.score = 0
				self.health = self.ship.ship_health()	
				
				pygame.mixer.music.load("assets/Game_song.wav")
				pygame.mixer.music.play(-1)

				for i in range(5):
					self.monster = monster.Monster("assets/trash (2).png")
					self.all_sprite.add(self.monster)

					self.trash.add(self.monster)
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

			hits = pygame.sprite.groupcollide(self.bullets,self.trash, True, True)
	
			if(hits):
				for hit in hits:					
					self.score += 10
					print(self.score)
					
					r = monster.Monster("assets/trash.png")
					self.all_sprite.add(r)
					self.trash.add(r)
					self.kill_counter += 1

					if (self.kill_counter % 10) == 0:
						s = monster.Monster("assets/trash.png")
						self.all_sprite.add(s)
						self.trash.add(s)
			
			phits = pygame.sprite.groupcollide(self.player,self.trash,False,True)
			for phit in phits:
				self.health -= 30
				if self.health < 0:
					self.show_init = True
					self.endgame_loop()
				

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
		"""
		This function carries out the operation of drawing onto any surface text. 
		args: surf (surface) which is the screen of our game in this case, it is where the text will be drawn onto. text (str) is the string of the text that is to be drawn onto a given surface. Size (int) is the size of the text, which will be needed to create the font object from pygame. x (int) is the x position that the text will be displayed in the game window. y (int) is the y position that the text will be displayed in the game window. 
		return: none
		"""
	
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text,True,self.white)
		text_rect = text_surface.get_rect()
		text_rect.centerx = x
		text_rect.top = y
		surf.blit(text_surface,text_rect)

	def start_loop(self):
		"""
		This function is the while loop in the starting screen that makes it so when the down key is pressed, the game will quit. When any other key is pressed, the game will start running again. This function also imports a song for the starting screen.
		args: none
		return: none			
		"""

		pygame.init()
		self.screen.blit(self.background_image, (0, 0))
		self.draw_text(self.screen,'Save the Sea',64,250,150)

		self.draw_text(self.screen,'\u2190 \u2192: Control movement of ship. Use space to shoot the bullet',15,250,250)
		
		self.draw_text(self.screen,'Press any key to start the game ! ',15,250,350)
		self.draw_text(self.screen,'Press ARROW DOWN to exit the game ',15,250,375)

		pygame.mixer.music.load("assets/Start_song.wav")
		pygame.mixer.music.play(-1)

		pygame.display.update()
		waiting = True
		while waiting:
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						pygame.quit()
				elif event.type == pygame.KEYUP:
					waiting = False 
	
	def endgame_loop(self):
		"""
		This function imports music for the ending screen. It also creates a json file and imports the json file into the end screen to record the highest score that the plaer made. This function can also allow the player to click down-ward to quit and press any other key to restart the game.
		args: none
		return: none
		"""
		pygame.init()

		pygame.mixer.music.load("assets/End_song.wav")
		pygame.mixer.music.play(-1)

		fptr = open("etc/Scores.json", "r")

		prev_scores = json.load(fptr)
		self.high_score = 0

		if prev_scores["Highest Score"] < self.score: 
			fptr.close()
			fptr2 = open("etc/Scores.json", "w")

			scores_dict = {}
			key = "Highest Score"
			
			scores_dict[key] = self.score
			self.high_score = self.score

			json.dump(scores_dict, fptr2)
			fptr2.close()
		else: 
			self.high_score = prev_scores["Highest Score"]			
			fptr.close()

		self.screen.blit(self.background_image, (0, 0))
		self.draw_text(self.screen,'Game Over! ',75,250,150)


		if self.high_score == self.score: 
			self.draw_text(self.screen,'Your Score is: '+ f'{self.score}' ,50,250,250)
			self.draw_text(self.screen, 'NICE! New High Score: ' + f'{self.high_score}', 25, 250, 312)

		else:
			self.draw_text(self.screen,'Your Score is: '+ f'{self.score}' ,50,250,250)
			self.draw_text(self.screen, 'Your High Score: ' + f'{self.high_score}', 25, 250, 312)
		
		self.draw_text(self.screen,'Press ARROW DOWN to EXIT the game',15,250,375)
		self.draw_text(self.screen,'Press any key to restart the game ! ',15,250,350)
		pygame.display.update()
		waiting = True
		while waiting:
			self.clock.tick(self.fps)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						pygame.quit()
				elif event.type == pygame.KEYUP:
					waiting = False 

					
					
	def draw_health(self,surf,hp,x,y):
		"""
		This function creates a red health bar for the ship with the health 100, and also sets a value for the hp lost whenever the garbage cans collides with the jet. This function also set up the positon of the health bar on the screen.
		args: surf(obj) screen object in this game is self.screen, hp(int) the health for the jet, x(int) x-axis for health bar's position, y(int) y-axis for health bar's position 
		return: none
		"""
		if hp < 0:
			hp = 0
		bar_length = 100
		bar_height = 10
		fill = (hp/100)*bar_length
		outline_rect = pygame.Rect(x,y,bar_length,bar_height)
		fill_rect = pygame.Rect(x,y,fill,bar_height)
		pygame.draw.rect(surf,self.red,fill_rect)
		pygame.draw.rect(surf,self.light_purple,outline_rect,2)
