import random
from src import weapon
import pygame
class Ship(pygame.sprite.Sprite):
	def __init__(self,img_file):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((50,40))
		#self.image.fill((0,255,0))

		ship_image = pygame.image.load(img_file).convert()

		self.image = pygame.transform.scale(ship_image, (53, 100))

		self.image.set_colorkey((255, 255, 255))
		

		self.rect = self.image.get_rect()
		self.rect.centerx = 250
		self.rect.bottom = 590
		self.speedx = 10
		self.health = 100
	
	def move_right(self): 
		"""
		This funciton create ship's horizontal moving speed, and prevent ship go over the screen. 
		arg: None
		return: None
		"""
		self.rect.x += self.speedx
		if self.rect.right > 500:
			self.rect.right = 500

	def move_left(self): 
		"""
		This function create ship's vertical moving speed, and prevent ship go over the screen.
		arg: None
		return: None
		"""
		self.rect.x -= self.speedx
		if self.rect.left < 0:
			self.rect.left = 0 

	def shipx(self): 
		"""
		This function stored ship's x-axis position
		arg: None
		return: self.rect.centerx (int)
		"""
		return self.rect.centerx 

	def shipy(self): 
		"""
		This function stored ship's y-axis position
		arg: None
		return: self.rect.top (int)
		"""
		return self.rect.top

	def ship_health(self): 
		"""		
		This function stored ship's heath 
		arg: None
		return: self.health(int)
		"""
		return self.health

