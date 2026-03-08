import pygame
import time

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((0,0),pygame.fullscreen)
pygame.display.set_caption("30-Second Counter")

# Font settings
font = pygame.font.Font(None, 80)  # Default font, size 80

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Timer
start_time = time.time()
countdown = 30

running = True
while running:
    screen.fill(WHITE)

    # Calculate remaining time
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(180 - elapsed_time, 0)

    # Render text
    text_surface = font.render(str(remaining_time), True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw text
    screen.blit(text_surface, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    # Stop when timer reaches 0
    if remaining_time == 0:
        pygame.time.delay(1000)
        running = False

pygame.quit()
