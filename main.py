import pygame
import sys
import random
import math

# Inicialización
pygame.init()

# Configuración básica
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DODGE-GAME")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
LIGHT_BLUE = (173, 216, 230)

# Variables del juego
player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)
enemies = [(random.randint(0, WIDTH), random.randint(-100, -40), 25) for _ in range(5)]
running = True

# Funciones

def draw_player(player_rect):
    top = (player_rect.centerx, player_rect.top)
    left = (player_rect.left, player_rect.bottom)
    right = (player_rect.right, player_rect.bottom)
    pygame.draw.polygon(screen, GOLD, [top, left, right])

def move_enemies(enemies):
    for i in range(len(enemies)):
        x, y, r = enemies[i]
        y += 5
        if y > HEIGHT:
            y = 0
            x = random.randint(0, WIDTH)
        enemies[i] = (x, y, r)

def detect_collision(player_rect, enemies):
    for enemy in enemies:
        x, y, r = enemy
        distance = math.sqrt((x - player_rect.centerx) ** 2 + (y - player_rect.centery) ** 2)
        if distance <= r + player_rect.width / 2:
            return True
    return False

def show_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, LIGHT_BLUE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(5000)  # Tiempo de espera antes de cerrar el juego

# Generador estrellas en el screen
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Bucle principal
while running:
    screen.fill(BLACK)
    
    # Dibujar estrellas
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += 5

    # Mover y dibujar enemigos
    move_enemies(enemies)
    for enemy in enemies:
        x, y, r = enemy
        pygame.draw.circle(screen, RED, (x, y), r)

    # Detección de colisiones
    if detect_collision(player, enemies):
        show_game_over()
        running = False

    # Dibujar jugador
    draw_player(player)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
