import pygame

# definir la classe qui gere les projectiles
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # faire tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si y a collision avec monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack)

        # condition pour verifier s'il sort de l'ecran
        if self.rect.x > 1080:
            self.remove()
