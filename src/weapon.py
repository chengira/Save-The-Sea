import random 
import pygame 
class Weapon(pygame.sprite.Sprite):

	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,20))
		self.image.fill((255,255,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.speedy= -10





        

	def update(self):

		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
