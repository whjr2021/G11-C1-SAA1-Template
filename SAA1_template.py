# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object
paddle = pygame.Rect(               )

# Create a rectangle for ball object 
ball = pygame.Rect(                 )

# Game loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Draw a golden colored paddle on screen
    pygame.draw.rect(screen,             ,       )
    
    # Draw an orange colored ball on screen
    pygame.draw.rect(screen,             ,       )
    
    # Update the display with paddle and ball objects
    pygame.display.update()