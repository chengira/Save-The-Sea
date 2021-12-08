import random
import pygame
class Monster(pygame.sprite.Sprite):
	def __init__(self,img_file):
		pygame.sprite.Sprite.__init__(self)


		monster_image = pygame.image.load(img_file).convert()

		self.image_ori = pygame.transform.scale(monster_image, (53, 60))

		self.image = self.image_ori.copy()

		self.image_ori.set_colorkey((255,255,255))

		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(10,470)
		self.rect.y = random.randrange(-100,-40)
		self.speedy = random.randrange(2,8)
		self.speedx = random.randrange(-3,3)
		
		self.total_degree = 0
		self.rot_degree = random.randrange(-3,3)

	def rotate(self): 
		"""
		This funciton make monsters roatate while they are moving.
		arg: None
		return: None
		"""
		self.total_degree += self.rot_degree
		self.total_degree = self.total_degree % 360
		self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
		center = self.rect.center 
		self.rect = self.image.get_rect()
		self.rect.center = center
	

	def update(self):
		"""
		This funciton sets monster's moving speed
		arg: None
		return: None
		"""
		self.rotate()
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > 600 or self.rect.left < 0 or self.rect.right >500:
			self.rect.x = random.randrange(10,470)
			self.rect.y = random.randrange(-100,-40)
			self.speedy = random.randrange(2,20)
			self.speedx = random.randrange(-3,3)
	
