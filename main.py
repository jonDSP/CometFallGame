import pygame
pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# generer la fenetre du jeu
pygame.display.set_caption("Comet Fall Game")
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

is_running = True

# creation de la boucle du jeu
while is_running:

    # detecter l'action de fermeture du jeu
    for event in pygame.event.get():  # renvoie une liste d'evenement, et on boucle dessus
        # si l'event detecté est la fermeture
        if event.type == pygame.QUIT:
            # on casse la boucle et on quitte proprement
            is_running = False
            pygame.quit()