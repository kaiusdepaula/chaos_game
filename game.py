from random import sample
import pygame

class Game():
    def __init__(self, width = 500, height = 500, dot_radius = int(1), dot_color = (0, 0, 0), game_bg_color = (255, 255, 255)):
        pygame.init()
        self.width, self.height = width, height
        self.running, self.playing, self.simulation = True, False, False
        self.display = pygame.Surface((self.width, self.height))
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font_name = pygame.font.get_default_font()
        self.START_KEY, self.ESCAPE_KEY = False, False

        self.dot_radius = dot_radius
        self.dot_color = dot_color
        self.game_bg_color = game_bg_color

        # Define a list to store the positions of the dots
        self.original_dots = []

    # Game loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.ESCAPE_KEY:
                self.playing = False
            if self.START_KEY:
                self.simulation = True

            if self.simulation:
                self.display.fill(self.game_bg_color)
                self.window.blit(self.display, (0, 0))
                self.original_dots = self.simulate()
            else:

                self.display.fill(self.game_bg_color)
                self.draw_text("Simulador de jogo do Caos", 30, self.width // 2, 30)
                self.draw_text("Aperte enter para continuar.", 20, self.width // 2, self.height - 20)
                self.window.blit(self.display, (0, 0))

                # Draw the dots on the display 
                for position in self.original_dots:
                    self.draw_dot(position)
            
            pygame.display.update()
            
            self.reset_keys()
    
    # Function to get events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Add the position of the mouse click to the list of dot positions
                self.original_dots.append(pygame.mouse.get_pos())
                pygame.display.update()

    # Reseting keys
    def reset_keys(self):
        self.START_KEY, self.ESCAPE_KEY = False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.dot_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    # Define a function to draw a dot at a given position
    def draw_dot(self, position):
        pygame.draw.circle(self.window, self.dot_color, position, self.dot_radius)

    # Define a function to handle simulation
    def simulate(self):
        
        more_dots = []
        # Draw a dot in the middle of two random dots
        if len(self.original_dots) >= 2:
            while self.simulation:

                self.check_events()
                if self.ESCAPE_KEY:
                    self.simulation = False
                self.reset_keys()

                first = True
                if first:
                    more_dots.extend(self.original_dots)
                    first = False
                # Choose two random dots from the list of dot positions
                dot1 = sample(self.original_dots, 1)[0]
                dot2 = sample(more_dots, 1)[0]
                # Calculate dot between the two dots
                dot_x = (dot1[0] + dot2[0]) // 2
                dot_y = (dot1[1] + dot2[1]) // 2
                dot_point = (dot_x, dot_y)

                # Draw a dot at the midpoint
                self.draw_dot(dot_point)

                # Add to list
                more_dots.append(dot_point)

                # Making sure all items are unique
                more_dots = list(set(more_dots))
                
                # Update display
                pygame.display.update()
        
        return(more_dots)