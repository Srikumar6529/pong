import pygame
from config import *
from rectangleshape import RectangleShape

class Pad(RectangleShape):
    def __init__(self,x,y,l,w):
        super().__init__(x,y,l,w)

    def draw(self, screen):
        pygame.draw.rect(screen,"white", (self.position.x,self.position.y,self.width,self.length),LINE_WIDTH)
    
    def update(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not self.position.y + self.length >= SCREEN_HEIGHT-10:
                self.position += pygame.Vector2(0,1) * dt * PLAYER_SPEED
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not self.position.y + self.length  <= PLAYER_LENGTH + 10:
                self.position += pygame.Vector2(0,1) * -dt * PLAYER_SPEED
