import random 
import pygame 

class Weapon(pygame.sprite.Sprite):

	def __init__(self,x,y,img_file):
		pygame.sprite.Sprite.__init__(self)
		bullet_image = pygame.image.load(img_file).convert()

		self.image = pygame.transform.scale(bullet_image, (9, 30))
		self.image.set_colorkey((255, 255, 255))

		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.speedy= -10

        

	def update(self):
		""" 
		This function sets the bullet's moving speed, and once it goes over the screen, it will disapear. It will update the bullet's position. 
		args: none
		return: none
		"""

		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
