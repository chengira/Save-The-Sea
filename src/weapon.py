import random 

class Weapon(pygame.sprite.Sprite):

    def init(self, name, x, y, img_file):

        pygame.sprite.Sprite.init(self)

        self.image = pygame.image.load(img_file).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 2

   def update(self):

      self.rect.x += self.speed
