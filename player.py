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