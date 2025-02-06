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

# importer la banniere
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

# importer un bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() / 2

# charger le jeu
game = Game()

is_running = True

# creation de la boucle du jeu
while is_running:

    # appliquer le background
    screen.blit(background, (0,-200))

    # verifier si le jeu a commencé
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


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

            # detecter si la touche espace est utilisée pour lancer projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si le bouton de la souris est en collision avec le bouton de jeu
            if play_button_rect.collidepoint(event.pos):
                game.start()