import random
import pygame
class Monster(pygame.sprite.Sprite):
	def __init__(self,img_file):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((30,40))
		#self.image.fill((255,0,0))


		monster_image = pygame.image.load(img_file).convert()

		self.image = pygame.transform.scale(monster_image, (53, 60))

		self.image.set_colorkey((255,255,255))

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
	
