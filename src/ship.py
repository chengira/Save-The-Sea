import random
import pygame
class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,40))
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 200
