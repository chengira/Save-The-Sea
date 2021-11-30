import random
import pygame
class Monster(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,40))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10,470)
		self.rect.y = random.randrange(-100,-40)
		self.speedy = random.randrange(2,8)
		self.speedx = random.randrange(-3,3)
	


	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > 600 or self.rect.left < 0 or self.rect.right >500:
			self.rect.x = random.randrange(10,470)
			self.rect.y = random.randrange(-100,-40)
			self.speedy = random.randrange(2,20)
			self.speedx = random.randrange(-3,3)
	
