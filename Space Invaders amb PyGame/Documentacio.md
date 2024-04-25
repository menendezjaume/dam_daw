# Space Invaders amb PyGame

## Pas 1: Instal·lació de PyGame

Primer, necessitaràs instal·lar PyGame. Això es pot fer fàcilment amb pip, l'eina de gestió de paquets de Python.

```bash
pip install pygame
```

## Pas 2: Configuració Bàsica

Crea un nou fitxer Python (per exemple, `space_invaders.py`) i comença amb una configuració bàsica.

```python
import pygame
import sys

# Inicialitzar PyGame
pygame.init()

# Configurar mida de la finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Títol de la finestra
pygame.display.set_caption("Space Invaders")

# Bucle principal del joc
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualitzar pantalla
    pygame.display.update()
```

## Pas 3: Afegir el Nau Espacial

Ara, afegeix una imatge de nau espacial al joc.

1. Descarrega o crea una imatge de nau espacial.
2. Carrega la imatge en el joc i col·loca-la a la part inferior de la pantalla.

```python
# Carregar imatge de la nau
ship = pygame.image.load('path/to/your/ship_image.png')
ship_rect = ship.get_rect(center=(width/2, height - 50))

# Dibuixar la nau
screen.blit(ship, ship_rect)
```

## Pas 4: Moviment de la Nau

Permet que els jugadors moguin la nau amb les tecles.

```python
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
```

## Pas 5: Execució del Joc a 60 FPS

Entendre, vols que tot el joc funcioni a 60 frames per segon (FPS). Això implicarà assegurar que el bucle principal del joc es repeteixi 60 vegades per segon. Aquí t'explico com implementar-ho.   

### 1. Establir un Relotge

Crea un rellotge a l'inici del teu script, que utilitzarem per controlar la taxa de frames.

```python
clock = pygame.time.Clock()
```

### 2. Bucle Principal del Joc

Dins del bucle principal, limitaràs el nombre de vegades que es pot actualitzar per segon utilitzant `clock.tick(60)`. Això assegura que independentment del que passi dins del bucle, no s'actualitzarà més de 60 vegades per segon.

```python
# Inicialitzar PyGame i crear la finestra...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Codi per actualitzar el joc, com ara moviment de la nau, disparar projectils, etc.

    pygame.display.update()
    clock.tick(60)  # Limita el joc a 60 frames per segon
```

### 3. Actualització de Moviments i Animacions

Quan programes el moviment de la nau, els projectils, i altres elements del joc, assegura't que la seva velocitat i comportament són consistents amb 60 FPS. Això significa que si vols que un objecte es mogui a una velocitat específica, hauràs de calcular la seva posició per cada frame considerant que el joc s'actualitza 60 vegades per segon.

### Notes Addicionals

- **Consistència en la Velocitat:** Assegura que tots els càlculs de moviment dins del joc prenguin en compte la taxa de 60 FPS per mantenir la consistència.
- **Prova de Rendiment:** Prova el joc en diferents sistemes per assegurar que es manté estable a 60 FPS.
- **Maneig de Diferents Taxes de Frames:** Si trobes que el joc no corre bé a 60 FPS en algunes màquines, potser necessitaràs ajustar el codi per manejar diferents taxes de frames de manera més dinàmica.

Executar el joc a 60 FPS garantirà una experiència de joc suau i més agradable per als jugadors.

## Pas 5: Animació de la nau

Per animar la nau, pots utilitzar sprites alternants que representen diferents estats de moviment. Per a això, necessitaràs dues imatges: una per a quan la nau està estàtica i una altra per a quan es mou.

### 1. Preparar les Imatges

Assegura't de tenir les dues imatges del propulsor:

1. **Imatge Propulsor Curt:** La primera imatge del propulsor.
2. **Imatge Propulsor Llarg:** La segona imatge del propulsor.

### 2. Carregar les Imatges

Carrega les dues imatges al principi del teu script.

```python
propulsor_curt = pygame.image.load('path/to/propulsor_curt.png')
propulsor_llarg = pygame.image.load('path/to/propulsor_llarg.png')
```

### 3. Alternar entre les Imatges

Utilitza una variable per controlar quina imatge del propulsor s'ha de mostrar. Alternaràs aquesta variable dins del bucle principal del joc.

```python
mostra_propulsor_llarg = False
```

### 4. Actualitzar i Dibuixar l'Animació

Dins del bucle principal del joc, actualitza la variable i dibuixa l'imatge del propulsor corresponent.

```python
# Dins del bucle principal del joc

    mostra_propulsor_llarg = not mostra_propulsor_llarg  # Alternar entre estats
    propulsor_actual = propulsor_llarg if mostra_propulsor_llarg else propulsor_curt
    screen.blit(propulsor_actual, (ship_rect.x + offset_x, ship_rect.y + offset_y))
```

Aquest codi alterna entre les dues imatges del propulsor en cada cicle del bucle del joc. `offset_x` i `offset_y` són les coordenades on vols dibuixar el propulsor respecte a la nau.

Per aconseguir una animació de 60 frames per segon, necessitaràs controlar la velocitat a la qual s'alternen les imatges del propulsor. Això es pot fer utilitzant un temporitzador. Vegem com implementar-ho.

### Implementació per 60 FPS

#### 1. Establir un Relotge

Primer, necessites crear un rellotge per controlar els frames per segon.

```python
clock = pygame.time.Clock()
```

#### 2. Alternar Imatges del Propulsor

Per alternar les imatges del propulsor a una taxa que compleixi amb 60 FPS, pots utilitzar una variable per comptar els frames i canviar les imatges a intervals regulars.

```python
frame_count = 0
mostra_propulsor_llarg = False
```

#### 3. Bucle Principal del Joc

Dins del teu bucle principal, actualitza la variable de frame i alterna les imatges.

```python
while True:
    # Resta del codi del bucle ...

    frame_count += 1
    if frame_count % 10 == 0:  # Canvia cada 10 frames (a 60 FPS, això és cada 1/6 de segon)
        mostra_propulsor_llarg = not mostra_propulsor_llarg

    propulsor_actual = propulsor_llarg if mostra_propulsor_llarg else propulsor_curt
    screen.blit(propulsor_actual, (ship_rect.x + offset_x, ship_rect.y + offset_y))

    pygame.display.update()
    clock.tick(60)  # Manté el joc a 60 FPS
```

Amb aquest codi, l'animació del propulsor canviarà aproximadament cada 1/6 de segon, donant la impressió d'una animació suau a 60 FPS.

#### Notes Addicionals

- **Ajust del Temporitzador:** Pots ajustar el nombre en `if frame_count % 10 == 0` per fer que l'animació sigui més ràpida o més lenta.
- **Sincronització amb el Joc:** Assegura't que la resta del joc també funcioni a 60 FPS per mantenir una experiència de joc uniforme.

Aquest enfocament assegura que l'animació del propulsor i la jugabilitat general del joc es mantenen suaus i consistents a 60 frames per segon.

## Pas 6: Afegir Enemics

El nostre objectiu és crear enemics que apareguin a la part superior de la pantalla i es moguin cap avall. Començarem definint una classe per als enemics, després crearem una llista d'enemics i finalment els afegirem al bucle principal del joc.

### 1. Definir la Classe Enemic

Primer, crearem una classe `Enemy` per gestionar les propietats i el comportament dels enemics.

```python
class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load('path/to/enemy_image.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
```

Aquesta classe inicialitza l'enemic amb una imatge i una posició. La funció `update` mou l'enemic cap avall.

### 2. Crear Llista d'Enemics

A continuació, crearem una llista per emmagatzemar múltiples enemics i els inicialitzarem en posicions diferents.

```python
enemies = []
enemy_rows = 3
enemy_cols = 5
enemy_x_spacing = 80
enemy_y_spacing = 60

for row in range(enemy_rows):
    for col in range(enemy_cols):
        x = col * enemy_x_spacing + 100
        y = row * enemy_y_spacing + 10
        enemies.append(Enemy(x, y))
```

Aquest codi crea una graella d'enemics, amb distàncies específiques entre ells.

### 3. Dibuixar i Actualitzar Enemics

Finalment, dibuixarem i actualitzarem els enemics dins del bucle principal del joc.

```python
# Dins del bucle principal del joc

    # Actualitzar i dibuixar cada enemic
    for enemy in enemies:
        enemy.update()
        screen.blit(enemy.image, enemy.rect)
```

Això assegura que cada enemic es mou i es dibuixa a cada iteració del bucle del joc.

### Notes Addicionals

- **Comprovació de Col·lisions:** Més endavant, hauràs d'afegir codi per comprovar col·lisions entre els projectils del jugador i els enemics.
- **Ajust de la Velocitat:** Pots ajustar la velocitat dels enemics canviant el valor de `self.speed` en la classe `Enemy`.
- **Imatges dels Enemics:** Assegura't que les imatges dels enemics siguin adequades i estiguin emmagatzemades en el camí especificat.

Aquesta és la base per afegir enemics al teu joc de Space Invaders. A mesura que els teus alumnes es tornin més còmodes amb PyGame i Python, poden experimentar amb diferents patrons de moviment, velocitats i fins i tot tipus d'enemics.

Per desenvolupar el Pas 6: Disparar Projectils, necessitarem crear una funcionalitat que permeti als jugadors disparar projectils per destruir els enemics. Això implica definir una classe per als projectils, gestionar l'emissió dels projectils i detectar col·lisions amb els enemics. Anem a veure-ho pas a pas.

## Pas 7: Disparar Projectils

### 1. Definir la Classe Projectil

Primer, crearem una classe `Projectile` per gestionar les propietats i el comportament dels projectils.

```python
class Projectile:
    def __init__(self, x, y):
        self.image = pygame.image.load('path/to/projectile_image.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
```

Aquesta classe crea un projectil amb una imatge i una posició inicial. La funció `update` mou el projectil cap amunt.

### 2. Gestionar l'Emissió de Projectils

A continuació, gestionarem l'emissió de projectils. Per fer-ho, necessitarem una llista per emmagatzemar els projectils actius i un mecanisme per afegir nous projectils quan el jugador premi una tecla.

```python
projectiles = []

# Dins del bucle principal del joc

    # Comprovar si es prem una tecla
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Crear un nou projectil
                projectile = Projectile(ship_rect.centerx, ship_rect.top)
                projectiles.append(projectile)
```

Aquest codi crea un nou projectil cada vegada que es prem la barra espaiadora.

### 3. Dibuixar i Actualitzar Projectils

Després, actualitzarem i dibuixarem els projectils dins del bucle principal del joc.

```python
# Dins del bucle principal del joc

    # Actualitzar i dibuixar cada projectil
    for projectile in projectiles:
        projectile.update()
        screen.blit(projectile.image, projectile.rect)

        # Eliminar projectils que surtin de la pantalla
        if projectile.rect.bottom < 0:
            projectiles.remove(projectile)
```

Això mantindrà la llista de projectils actualitzada, eliminant aquells que ja no es veuen a la pantalla.

### 4. Detectar Col·lisions

Finalment, hauràs d'afegir codi per detectar col·lisions entre els projectils i els enemics.

```python
# Dins del bucle principal del joc

    # Comprovar col·lisions
    for projectile in projectiles:
        for enemy in enemies:
            if projectile.rect.colliderect(enemy.rect):
                projectiles.remove(projectile)
                enemies.remove(enemy)
                break
```

Aquest codi comprova si algun projectil xoca amb un enemic, i en cas afirmatiu, elimina tant el projectil com l'enemic.

### Notes Addicionals

- **Imatges dels Projectils:** Assegura't que les imatges dels projectils siguin adequades i estiguin emmagatzemades en el camí especificat.
- **Optimització:** Pot ser necessari optimitzar el codi per manejar una gran quantitat de projectils i enemics, especialment per evitar l'ús excessiu de recursos.

Amb aquestes pautes, els teus alumnes podran implementar una funcionalitat clau en el seu joc de Space Invaders, afegint una capa més d'interacció i desafiament al joc.

Per al Pas 7, desenvoluparem un sistema de puntuació i vides per al joc de Space Invaders. Aquest sistema aporta elements addicionals d'estratègia i competència, fent el joc més emocionant. Anem a veure com implementar això.

### Pas 8: Sistema de Puntuació i Vides

#### 1. Inicialitzar Puntuació i Vides

Comencem per definir variables globals per a la puntuació i el nombre de vides.

```python
score = 0
lives = 3
```

Aquestes variables es poden ajustar segons el nivell de dificultat que vulguis.

#### 2. Mostrar Puntuació i Vides

Utilitzarem funcions de PyGame per mostrar la puntuació i les vides a la pantalla.

```python
font = pygame.font.Font(None, 36)

def draw_score():
    score_text = font.render(f"Puntuació: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def draw_lives():
    lives_text = font.render(f"Vides: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (width - 120, 10))
```

Aquestes funcions renderitzen la puntuació i les vides com a text i les dibuixen a la pantalla.

#### 3. Actualitzar Puntuació

Quan un enemic és destruït, actualitzarem la puntuació.

```python
# Dins del bucle principal del joc, a la secció de detecció de col·lisions

            if projectile.rect.colliderect(enemy.rect):
                projectiles.remove(projectile)
                enemies.remove(enemy)
                score += 10  # Augmentar puntuació
                break
```

Aquesta secció del codi augmenta la puntuació cada vegada que un enemic és destruït.

#### 4. Gestionar les Vides

Les vides es reduiran quan un enemic arribi a la part inferior de la pantalla o quan el jugador sigui colpejat.

```python
# Dins del bucle principal del joc

    for enemy in enemies:
        enemy.update()
        if enemy.rect.bottom > height:
            lives -= 1
            enemies.remove(enemy)

        # Aquí també es podria afegir la lògica per comprovar si l'enemic colpeja la nau del jugador
```

Aquest codi redueix una vida quan un enemic travessa la pantalla.

#### Notes Addicionals

- **Ajusta la Dificultat:** Pots ajustar la dificultat del joc canviant la puntuació obtinguda per enemic destruït o el nombre de vides inicials.
- **Disseny Gràfic:** Considera afegir elements gràfics com coracions o altres ícones per representar les vides.
- **Guardar la Millor Puntuació:** Com a extensió, podríeu implementar una manera de guardar la millor puntuació entre les partides.

Amb aquestes funcionalitats, el joc de Space Invaders serà més complet, oferint als jugadors una experiència més rica i desafiant.

#### 5. Finalitzar el Joc

Finalment, afegeix una condició de finalització del joc quan el jugador es queda sense vides.

```python
# Dins del bucle principal del joc

    if lives <= 0:
        pygame.quit()
        sys.exit()
```

Aquest codi finalitza el joc quan el jugador es queda sense vides.

## Pas 9: Polir i Optimitzar

Revisa el codi, afegeix comentaris i realitza optimitzacions si és necessari.

## Recursos Addicionals

- **Documentació de PyGame:** Una gran font per aprendre més sobre les funcionalitats específiques de PyGame.
- **Tutorials en línia:** Hi ha molts tutorials gratuïts disponibles que poden ajudar a comprendre millor com utilitzar PyGame.

Recorda que la pràctica i l'experimentació són claus en l'aprenentatge de la programació. Encoratja els teus alumnes a ser creatius i a provar coses noves mentre treballen en aquest projecte.
