import random 
import pygame 
class Weapon(pygame.sprite.Sprite):

	def __init__(self,x,y,img_file):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10,20))
		#self.image.fill((255,255,0))
		bullet_image = pygame.image.load(img_file).convert()

		self.image = pygame.transform.scale(bullet_image, (9, 30))
		self.image.set_colorkey((255, 255, 255))

		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.speedy= -10

		



        

	def update(self):

		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
