# In Alien Invasion, the player controls a ship that appears at 
# the bottom center of the screen. The player can move the ship 
# right and left using the arrow keys and shoot bullets using the 
# spacebar. When the game begins, a fleet of aliens fills the sky 
# and moves across and down the screen. The player shoots and 
# destroys the aliens. If the player shoots all the aliens, a new fleet 
# appears that moves faster than the previous fleet. If any alien hits 
# the player’s ship or reaches the bottom of the screen, the player 
# loses a ship. If the player loses three ships, the game ends.

import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
 # Initialize game and create a screen object.
 pygame.init()
 ai_settings = Settings()

 screen = pygame.display.set_mode(
   (ai_settings.screen_width, ai_settings.screen_height))
 pygame.display.set_caption("Alien Invasion")
 
 # Make a ship.
 ship = Ship(ai_settings, screen)
 
 # Start the main loop for the game.
 while True:
    gf.check_events(ship)
    ship.update()
    gf.update_screen(ai_settings, screen, ship)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        sys.exit()
 # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
 # Make the most recently drawn screen visible.
    pygame.display.flip()
run_game()
