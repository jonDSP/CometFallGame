import pygame
from player import Player

# creer une classe du jeu
class Game:
    def __init__(self):
        # generer le joueur
        self.player = Player()
        self.pressed = {}