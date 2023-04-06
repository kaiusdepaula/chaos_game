import pygame
import random
from time import sleep

# Initialize Pygame
pygame.init()

# Define the window size
win_width, win_height = 512, 768
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Simulador de jogo do Caos")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the radius of the dots to be drawn
DOT_RADIUS = 1

# Define the Pygame clock
clock = pygame.time.Clock()

# Define a list to store the positions of the dots
original_dots = []

# Define a function to draw a dot at a given position
def draw_dot(position):
    pygame.draw.circle(win, WHITE, position, DOT_RADIUS)

# Define a function to update the display
def update_display():

    win.fill(BLACK)
    # Draw the dots on the display 
    for position in original_dots:
        draw_dot(position)

    # Display the message on the screen
    font = pygame.font.SysFont('arial', 20)
    text = font.render("Aperte espaço para continuar.", True, WHITE)
    text_width, text_height = text.get_size()
    win.blit(text, ((win_width - text_width) // 2, 20))

    pygame.display.update()

# Define a function to handle button presses
def handle_button_press():

    win.fill(BLACK)
    # Draw the dots on the display 
    for position in original_dots:
        draw_dot(position)

    more_dots = []
    drawing = True  # Set drawing to True before starting to draw dots
    # Original drawing speed
    speed = 1

    # Draw a dot in the middle of two random dots
    if len(original_dots) >= 2:
        while drawing:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    drawing = False  # Set drawing to False when spacebar is pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    speed = 0.005
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    speed = 0.2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    speed = 1

            first = True
            if first:
                more_dots.extend(original_dots)
                first = False
            # Choose two random dots from the list of dot positions
            dot1 = random.sample(original_dots, 1)[0]
            dot2 = random.sample(more_dots, 1)[0]
            # Calculate the midpoint between the two dots
            mid_x = (dot1[0] + dot2[0]) // 2
            mid_y = (dot1[1] + dot2[1]) // 2
            mid_point = (mid_x, mid_y)

            # Draw a dot at the midpoint
            draw_dot(mid_point)

            # Add to list
            more_dots.append(mid_point)

            # Making sure all items are unique
            more_dots = list(set(more_dots))

            # Update display
            pygame.display.update()
            sleep(speed)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add the position of the mouse click to the list of dot positions
            original_dots.append(pygame.mouse.get_pos())
            update_display()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                handle_button_press()     

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
