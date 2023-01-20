import pygame
import random as r

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('My Game')

# Set the background color of the screen
bg_color = (255, 255, 255)

# Load the example logo image
logo = pygame.image.load('example logo.png')

# Get the rectangle that represents the example logo's position and size
logo_rect = logo.get_rect()

# Set the starting position and speed of the example logo
logo_rect.x = r.randint(200, screen_width - 200)
logo_rect.y = r.randint(200, screen_height - 200)
speed_x = 2 * r.choice([-1, 1])
speed_y = 1 * r.choice([-1, 1])

# Main game loop
running = True
while running:
    # Fill the screen with the background color
    screen.fill(bg_color)

    # Draw the example logo on the screen
    screen.blit(logo, logo_rect)

    # Handle events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the example logo
    logo_rect.x += speed_x
    logo_rect.y += speed_y

    # Check if the example logo has hit a wall and needs to bounce
    if logo_rect.left < 0 or logo_rect.right > screen_width:
        speed_x = -speed_x
    if logo_rect.top < 0 or logo_rect.bottom > screen_height:
        speed_y = -speed_y

    # Update the screen
    pygame.display.flip()

# Close the window and quit
pygame.quit()
