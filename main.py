import pygame
import game
import button

# Initialize Pygame
pygame.init()

# Define the window size
win_width, win_height = 512, 768
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Simulador de jogo do Caos")

# Create main menu button instances
start_button = button.button(x = win_width // 3, y = 2 * win_height // 6, width=200, height=50, text='Iniciar', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
options_button = button.button(x = win_width // 3, y = 3 * win_height // 6, width=200, height=50, text='Opções', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
exit_button = button.button(x = win_width // 3, y = 4 * win_height // 6, width=200, height=50, text='Sair', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))

# Create options menu button instances
return_button = button.button(x = win_width // 6, y = win_height * 4 // 5, width=350, height=50, text='Retornar ao menu inicial', font_size=25, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
classic_button = button.button(x = win_width // 2 - 170, y = win_height // 2, width=75, height=50, text='1/2', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
two_by_three_button = button.button(x = win_width // 2 + 100, y = win_height // 2, width=75, height=50, text='2/3', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
phi_jump_button = button.button(x = win_width // 2 - 50, y = win_height // 2, width=120, height=50, text='phi', font_size=25, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))

# Define the Pygame clock
clock = pygame.time.Clock()

# Color variable
BLACK = (0, 0, 0)

# Main menu loop
options = False
g = game.Game(win_width, win_height)


while g.running:
        win.fill(BLACK)
        g.original_dots = []
        if start_button.draw(win):
            g.playing = True
            g.game_loop()
        if options_button.draw(win):
            options = True
        if exit_button.draw(win):
            g.running = False

        while options:
            win.fill(BLACK)

            if return_button.draw(win):
                options = False
            if classic_button.draw(win):
                g.jump = 0.5
                options = False
            if two_by_three_button.draw(win):
                g.jump = float(2 / 3)
                options = False
            if phi_jump_button.draw(win):
                g.jump = float(1 / 1.618)
                options = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False
                    options = False
            pygame.display.update()

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.running = False
        # Limit the frame rate
        clock.tick(60)
        pygame.display.update()

# Quit Pygame
pygame.quit()
