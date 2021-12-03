import random
from src import weapon
import pygame
class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,40))
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = 250
		self.rect.bottom = 590
		self.speedx = 8
	


	def update(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[pygame.K_RIGHT]:
			self.rect.x += 2
		if key_pressed[pygame.K_LEFT]:
			self.rect.x -= 2
		



		if self.rect.right > 500:
			self.rect.right = 500
		if self.rect.left < 0:
			self.rect.left = 0 
	def shoot(self):
		return weapon.Weapon(self.rect.centerx,self.rect.top)
