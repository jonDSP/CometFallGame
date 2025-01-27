import pygame
from game import Game
pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


# generer la fenetre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# charger l'arriere plan
background = pygame.image.load("assets/bg.jpg")

# charger le jeu
game = Game()

is_running = True

# creation de la boucle du jeu
while is_running:

    # appliquer le background
    screen.blit(background, (0,-200))

    # appliquer le jueur
    screen.blit(game.player.image,game.player.rect)

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width< screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre a jour l'ecran
    pygame.display.flip()

    # detecter l'action de fermeture du jeu
    for event in pygame.event.get():  # renvoie une liste d'evenement, et on boucle dessus
        # si l'event detecté est la fermeture
        if event.type == pygame.QUIT:
            # on casse la boucle et on quitte proprement
            is_running = False
            pygame.quit()

        # detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False