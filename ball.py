import pygame,random
from circleshape import CircleShape
from config import *
class Ball(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x,y,BALL_RADIUS)
        self.velocity = pygame.Vector2(BALL_SPEED,BALL_SPEED)
        self.velocity = self.velocity.rotate(random.randrange(0,361))
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt,pads):
        self.position += dt * self.velocity
        if self.position.y - self.radius <= 0:
           self.velocity. y = -1 * self.velocity.y
        elif self.position.y + self.radius >= SCREEN_HEIGHT:
            self.velocity. y = -1 * self.velocity.y
        if self.position.x - self.radius <= 0:
           self.velocity. x = -1 * self.velocity.x
        elif self.position.x + self.radius >= SCREEN_WIDTH:
            self.velocity. x = -1 * self.velocity.x
