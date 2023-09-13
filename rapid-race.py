import pygame
import time
import random

pygame.init()

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rapid Race")

# Cargar imágenes
car_img = pygame.image.load("car.png")
grass = pygame.image.load("grass.jpg")
yellow_strip = pygame.image.load("yellow_strip.jpg")
strip = pygame.image.load("strip.jpg")

# Imágenes de obstáculos
obstacle_images = [
    pygame.image.load("neumatico.png"),
    pygame.image.load("poste.png"),
    pygame.image.load("barril.png"),
    pygame.image.load("pared.png"),
    pygame.image.load("vaca.png"),
    pygame.image.load("policia.png")
]

# Mensaje de choque
myfont = pygame.font.SysFont("None", 100)
render_text = myfont.render("¡YOU LOST!", 1, (100, 0, 0))

# Reloj para controlar la velocidad
clock = pygame.time.Clock()

# Tamaño del carro y obstáculos
car_width = 80
car_height = 100

# Redimensionar el carro
car_img = pygame.transform.scale(car_img, (car_width, car_height))

# Función para dibujar el carro en la pantalla
def car(x, y):
    screen.blit(car_img, (x, y))

# Función para dibujar el fondo
def background():
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(yellow_strip, (376.5, 0))
    screen.blit(yellow_strip, (376.5, 100))
    screen.blit(yellow_strip, (376.5, 200))
    screen.blit(yellow_strip, (376.5, 300))
    screen.blit(yellow_strip, (376.5, 400))
    screen.blit(yellow_strip, (376.5, 500))
    screen.blit(yellow_strip, (376.5, 600))
    screen.blit(strip, (120, 0))
    screen.blit(strip, (680, 0))

# Función para dibujar obstáculos
def obstacle(obs_x, obs_y, obs_type):
    obs_pic = obstacle_images[obs_type]
    obs_pic = pygame.transform.scale(obs_pic, (car_width, car_height))  # Redimensionar el obstáculo
    screen.blit(obs_pic, (obs_x, obs_y))

# Función para crear obstáculos aleatorios
def create_obstacle():
    obs_x = random.randrange(200, 650)
    obs_y = -100
    obs_speed = 5
    obs_type = random.randint(0, 5)
    return obs_x, obs_y, obs_speed, obs_type

# Inicializar el estado del juego
def game_loop():
    x = 360
    y = 500
    x_change = 0
    bumped = False

    obs_x, obs_y, obs_speed, obs_type = create_obstacle()

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # Limitar la posición del carro dentro del carril
        if x < 110:
            x = 110
        elif x > 680 - car_width:
            x = 680 - car_width

        screen.fill((119, 119, 119))
        background()

        # Mover y dibujar obstáculos
        obs_y += obs_speed
        obstacle(obs_x, obs_y, obs_type)

        car(x, y)

        # Verificar colisión con el obstáculo
        if y < obs_y + car_height:
            if x > obs_x and x < obs_x + car_width or x + car_width > obs_x and x + car_width < obs_x + car_width:
                screen.blit(render_text, (100, 200))
                pygame.display.update()
                time.sleep(5)
                bumped = True
                game_loop()

        # Verificar si el obstáculo ha pasado al final de la pantalla
        if obs_y > height:
            obs_x, obs_y, obs_speed, obs_type = create_obstacle()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()