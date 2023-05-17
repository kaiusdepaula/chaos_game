import pygame
import game
import button

# Images directory
images_dir = "images/"

# Initialize Pygame
pygame.init()

# Colors
ROSE = (243, 225, 221)
RICH_BLACK = (2, 17, 27)
ONYX = (63, 64, 69)
MOONSTONE = (88, 164, 176)

# Define the window size
win_width, win_height = 512, 768
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Simulador de jogo do Caos")

# Create main menu button instances
start_button = button.button(
    x = (win.get_width() - 200) // 2, 
    y = (win.get_height() - 400), 
    width=200, 
    height=50, 
    text='Iniciar', 
    font_size=32, 
    font_style='Arial', 
    bg_color= MOONSTONE, 
    text_color= RICH_BLACK
)
more_about_button = button.button(
    x = (win.get_width() - 200) // 2, 
    y = (win.get_height() - 300), 
    width=200, 
    height=50, 
    text='Sobre', 
    font_size=32, 
    font_style='Arial', 
    bg_color= MOONSTONE, 
    text_color= RICH_BLACK
)
exit_button = button.button(
    x = (win.get_width() - 200) // 2, 
    y = (win.get_height() - 200), 
    width=200, 
    height=50, 
    text='Sair', 
    font_size=32, 
    font_style='Arial', 
    bg_color= MOONSTONE, 
    text_color= RICH_BLACK
)
return_button = button.button(
    x = (win.get_width() - 200) // 2, 
    y = win_height - 100, 
    width=200, 
    height=50, 
    text='Retornar', 
    font_size=32, 
    font_style='Arial', 
    bg_color= MOONSTONE, 
    text_color= RICH_BLACK
)

font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

texto = """
    Fractais são maravilhas matemáticas hipnotizantes. 
    O Jogo do Caos, uma abordagem cativante, gera padrões intricados através de uma dança delicada 
    entre aleatoriedade e precisão. A cada iteração, pontos convergem, revelando auto similaridade dentro 
    da complexidade. Contemple a beleza dos fractais se desdobrando, onde a ordem emerge do caos e a 
    complexidade infinita reside em formas finitas.
    """

# Wrap the long text into multiple lines
words = texto.split()
wrapped_lines = []
current_line = ""
for word in words:
    if font.size(current_line + word)[0] <= win.get_width() - 2 * 20:
        current_line += word + " "
    else:
        wrapped_lines.append(current_line)
        current_line = word + " "
    if '.' in word:
        wrapped_lines.append(current_line)
        current_line = ""
wrapped_lines.append(current_line)

# Render the wrapped text
text_surfaces = [font.render(line, True, RICH_BLACK) for line in wrapped_lines]

# Calculate the position to center the text on the screen
total_height = sum(surface.get_height() for surface in text_surfaces)
y = (win.get_height() - total_height) // 2


# Render the title
title_surface = title_font.render("Sobre o Jogo do Caos e os Fractais", True, RICH_BLACK)
title_x = (win.get_width() - title_surface.get_width()) // 2
title_y = 40


# Render the small text
small_text = "App criado por Kaius de Paula Corrêa."
small_surface = font.render(small_text, True, RICH_BLACK)
small_x = (win.get_width() - small_surface.get_width()) // 2
small_y = win.get_height() - 200 - small_surface.get_height()

# Load Chaos Game logo
image = pygame.image.load(images_dir + "chaos_game_logo.png")
# Define the desired scale factor
scale_factor = 0.3
# Resize the image
image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))


# Load Chaos Game Title
title = pygame.image.load(images_dir + "Titulo.png")


# Define the Pygame clock
clock = pygame.time.Clock()

# Instanciate Game object
g = game.Game(
    win_width, 
    win_height,
    dot_color = RICH_BLACK, 
    game_bg_color = ROSE
)

# The second menu should be off 
more_about = False

while g.running:
        win.fill(ROSE)

        # Blit title and logo onto the screen
        win.blit(image, ((win.get_width() - image.get_width()) // 2, 50))
        win.blit(title, ((win.get_width() - title.get_width()) // 2, image.get_height() + 60))

        g.original_dots = []
        if start_button.draw(win):
            g.playing = True
            g.game_loop()
        if more_about_button.draw(win):
            more_about = True
        if exit_button.draw(win):
            g.running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False
                    options = False
            pygame.display.update()
        
        while more_about:
            win.fill(ROSE)

            # Blit the title onto the screen
            win.blit(title_surface, (title_x, title_y)) 
            # Blit the wrapped text onto the screen
            for surface in text_surfaces:
                win.blit(surface, (win.get_width() // 2 - surface.get_width() // 2, y))
                y += surface.get_height()
            
            # Reset the y position for the next frame
            y = (win.get_height() - total_height) // 2

            # Blit the small text onto the screen
            win.blit(small_surface, (small_x, small_y))

            if return_button.draw(win):
                more_about = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False
                    more_about = False
            
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
