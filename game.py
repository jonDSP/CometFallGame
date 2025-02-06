import pygame
from player import Player
from monster import Monster

# creer une classe du jeu
class Game:
    def __init__(self):
        # definir si le jeu a commencé ou non
        self.is_playing = False
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # defininr un gfroupe de monstrer
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu a neuf (vie max, erase les monstres)
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer le joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre du joueur
        self.player.update_health_bar(screen)

        # recuperr les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # appliquer les images du groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer le groupe de monstrer
        self.all_monsters.draw(screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)