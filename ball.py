import pygame,random
from circleshape import CircleShape
from config import *
import sys
class Ball(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x,y,BALL_RADIUS)
        unitvector = pygame.Vector2(0,1)
        self.velocity = unitvector * BALL_SPEED
        self.velocity = self.velocity.rotate(random.randrange(0,361))
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def scores(self,x,y):
        print(f"player 1: {x}")
        print(f"player 2: {y}")
    def update(self,dt,pads):
        self.position += dt * self.velocity
        if self.position.y - self.radius <= 0:
           self.velocity. y = -1 * self.velocity.y
        elif self.position.y + self.radius >= SCREEN_HEIGHT:
            self.velocity. y = -1 * self.velocity.y
        elif self.position.x - self.radius <= 0:
           #self.velocity. x = -1 * self.velocity.x
           print("GAME OVER!!!!")
           pads[1].score += 1
           self.scores(pads[0].score,pads[1].score)
           sys.exit()
        elif self.position.x + self.radius >= SCREEN_WIDTH:
            #self.velocity. x = -1 * self.velocity.x
            print("GAME OVER!!!")
            pads[0].score += 1
            self.scores(pads[0].score,pads[1].score)
            sys.exit()
        else:
            for pad in pads:
                x,y = pad.position.x + pad.width //2, pad.position.y + pad.length //2
                dist = (self.position.x - x) ** 2 + (self.position.y - y) ** 2
                dist = dist ** .5

                if dist <= (self.radius + pad.width):
                    self.velocity.x = -1 * self.velocity.x
                    self.velocity.y = -1 * self.velocity.y
                    return


