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
	
	def move_right(self): 
		self.rect.x += self.speedx
		if self.rect.right > 500:
			self.rect.right = 500

	def move_left(self): 
		self.rect.x -= self.speedx
		if self.rect.left < 0:
			self.rect.left = 0 

	def shipx(self): 
		return self.rect.centerx 

	def shipy(self): 
		return self.rect.top
