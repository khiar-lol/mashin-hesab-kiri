import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
screen_width = 800
screen_height = 600
circle_color = (255, 0, 0)
background_color = (255, 255, 255)
circle_radius = 30

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("توپ کصخل")

# Circle starting position
circle_x = screen_width // 2
circle_y = screen_height // 2
circle_speed_x = 5
circle_speed_y = 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the circle
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # Bounce the circle off the walls
    if circle_x - circle_radius < 0 or circle_x + circle_radius > screen_width:
        circle_speed_x = -circle_speed_x
    if circle_y - circle_radius < 0 or circle_y + circle_radius > screen_height:
        circle_speed_y = -circle_speed_y

    # Fill the background
    screen.fill(background_color)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)