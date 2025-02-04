import pygame
from projectile import Projectile

# creer un classe representant le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.attack = 5
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self,amount):
        if self.health - amount > 0:
            self.health -= amount

    def update_health_bar(self, surface):
        # dessiner la barre arriere
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y +20 , self.max_health, 7])
        # dessiner la barre de vie
        pygame.draw.rect(surface, (110, 210, 46), [self.rect.x + 50, self.rect.y +20, self.health, 7])

    def launch_projectile(self):
        # creer une nouvelle instance de Projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        # deplacement que si il n'y a pas de collision avec monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity