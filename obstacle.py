import pygame
import settings as s
from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init__(self,x,y,width,speed,direction,jumpable,color):
        super(Obstacle, self).__init__()
        self.x =        x
        self.y =        y
        self.width =    width
        self.speed =    (1 if direction is 'right' else -1) * speed/1000
        self.jumpable = jumpable
        self.color =    color
        self.rect =     pygame.Rect(self.x,self.y,self.width,s.obstacle_height)
        
        
    def move(self,dt):
        self.x += self.speed * dt
        self.rect.x = self.x
        
    def update(self,dt):
        self.move(dt)
    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)