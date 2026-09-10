import pygame
from config import PADDLE_SPEED, LINE_WIDTH, PADDLE_LENGTH, PADDLE_WIDTH, SCREEN_HEIGHT
from rectangleshape import RectangleShape

class Pad(RectangleShape):
    def __init__(self,x,y,l,w,controls):
        super().__init__(x,y,l,w)
        self.controls = controls
    def draw(self, screen):
        pygame.draw.rect(screen,"white", (self.position.x,self.position.y,self.width,self.length),LINE_WIDTH)
    
    def update(self,dt):
        x,y = self.position.x + self.width//2 , self.position.y + self.length //2
        keys = pygame.key.get_pressed()

        if keys[self.controls["down"]]:
            if not y + self.length//2 >= SCREEN_HEIGHT-10:
                self.position += pygame.Vector2(0,1) * dt * PADDLE_SPEED
        if keys[self.controls["up"]]:
            if not y + self.length//2  <= PADDLE_LENGTH + 10:
                self.position += pygame.Vector2(0,1) * -dt * PADDLE_SPEED
