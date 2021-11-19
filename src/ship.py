import random

class Ship(pygame.sprite.Sprite):

    def init(self, name, x, y, img_file):
        
        pygame.sprite.Sprite.init(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.name = name
        self.speed = 3
        self.health = 10

   
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def fire(self):

        if(random.randrange(3)):
            self.health -= 1
            print("Attack Failed. Remaining Health: ", self.health)
            return False
        else:
            print("Attack Successful")
        return True
