"""Show the game are won by the user."""
import pygame

class GameWon():
    """Show when the game are won."""
    
    def __init__(self, screen):
        """Initialize game won attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 500, 50
        self.message_box_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 38)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once.
        self.prep_msg("Congratulation!!! You Won!!!")
        
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.message_box_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_message(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.message_box_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
