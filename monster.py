import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(0, 3)
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        self.health -= amount

        # verifier si le nbre de points de vie tombe a 0
        if self.health <= 0:
            # faire un reset du monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

    def update_health_bar(self, surface):

        # dessiner la barre arriere
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])

        # dessiner la barre de vie
        pygame.draw.rect(surface, (110, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])



    def forward(self):
        # le deplacement ne se fait que si'il n'ya pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # si le monstre entre en collision avec le joueur , on applique les degats
            self.game.player.damage(self.attack)

