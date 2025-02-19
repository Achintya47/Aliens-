
import sys
import pygame
from Settings import Setting
from Spaceship import Ship

class AlienInversion:   
    def __init__(self):
        pygame.init()
        self.set=Setting()
    
        self.screen=pygame.display.set_mode((self.set.screen_height,self.set.screen_width))
        pygame.display.set_caption("Alien Inversion")
        self.ship=Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    self.ship.moving_right=True
                elif event.key==pygame.K_a:
                    self.ship.moving_left=True
                elif event.key==pygame.K_w:
                    self.ship.moving_Up=True
                elif event.key==pygame.K_s:
                    self.ship.moving_Down=True
                elif event.key==pygame.K_SPACE:
                    self.ship.rect.y-=50
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_d:
                    self.ship.moving_right=False
                elif event.key==pygame.K_a:
                    self.ship.moving_left=False
                elif event.key==pygame.K_w:
                    self.ship.moving_Up=False
                elif event.key==pygame.K_s:
                    self.ship.moving_Down=False

    
    def _update_screen(self):
        self.screen.fill(self.set.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__=="__main__":
    ai=AlienInversion()
    ai.run_game()