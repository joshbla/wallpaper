import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size and title
window_size = (800, 800)
pygame.display.set_caption("Psychedelic Circle")

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the circle's starting position and velocity
x, y = 400, 400
vx, vy = random.uniform(-3, 3), random.uniform(-3, 3)

# Run the game loop
running = True
while running:
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Update the circle's position
    x += vx
    y += vy
    
    # Bounce the circle off the edges of the window
    if x < 0 or x > window_size[0]:
        vx = -vx
    if y < 0 or y > window_size[1]:
        vy = -vy
    
    # Draw the circle
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, color, (int(x), int(y)), 50)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
