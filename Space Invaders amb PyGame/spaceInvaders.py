import pygame
import sys

# Inicialitzar PyGame
pygame.init()

# Configurar mida de la finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Títol de la finestra
pygame.display.set_caption("Space Invaders")

# Carregar les imatges de la nau
propulsor_curt = pygame.image.load('anvion0-rotado.png')
propulsor_llarg = pygame.image.load('anvion1-rotado.png')

mostra_propulsor_llarg = False

# Inicialitzar amb la imatge estàtica
ship = propulsor_curt
ship_rect = ship.get_rect(center=(width/2, height - 100))

# Dibuixar la nau
# screen.blit(ship, ship_rect)

clock = pygame.time.Clock()
frame_count = 0

# Bucle principal del joc
while True:
    frame_count += 1

    # Canvia cada 10 frames (a 60 FPS, això és cada 1/6 de segon)
    if frame_count % 5 == 0:
        mostra_propulsor_llarg = not mostra_propulsor_llarg
    # mostra_propulsor_llarg = not mostra_propulsor_llarg  # Alternar entre estats
    ship = propulsor_llarg if mostra_propulsor_llarg else propulsor_curt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dins del bucle principal

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= 5  # Moure a l'esquerra
    if keys[pygame.K_RIGHT]:
        ship_rect.x += 5  # Moure a la dreta

    # Assegurar que la nau no surti de la pantalla
    ship_rect.x = max(ship_rect.x, 0)
    ship_rect.x = min(ship_rect.x, width - ship.get_width())

    # Dibuixar la nau
    screen.fill((0, 0, 0))  # Fons negre
    screen.blit(ship, ship_rect)

    # Actualitzar pantalla
    pygame.display.update()
    clock.tick(60)  # Limita el joc a 60 frames per segon
