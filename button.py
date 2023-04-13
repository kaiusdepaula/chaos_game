import pygame

class button:
    pygame.font.init()
    def __init__(self, x, y, width, height, text='', font_size=30, font_style=None, bg_color=(255, 255, 255), text_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font_style, font_size) if font_style else pygame.font.Font(None, font_size)
        self.clicked = False
    
    # Draw method
    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # And check if clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        # Draw button on screen
        pygame.draw.rect(surface, self.bg_color, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
    
        return action

# USAGE EXAMPLE
# my_button = button(x=100, y=100, width=200, height=50, text='Click me!', font_size=32, font_style='Arial', bg_color=(255, 255, 255), text_color=(0, 0, 0))
