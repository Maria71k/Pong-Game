import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Initialize variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-1, 1])
ball_dy = random.choice([-1, 1])
paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Collision detection with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy *= -1

    # Collision detection with paddles
    if ball_x <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    elif ball_x >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Ball goes out of bounds
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx *= random.choice([-1, 1])
        ball_dy *= random.choice([-1, 1])

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
