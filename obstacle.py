import pygame
import settings as s
from pygame.sprite import Sprite

'''Obstacle class to be used with any moving objects except the frog.'''
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
        
    '''Method that moves the object horizontal to the screen based on given speed.'''
    def move(self,dt):
        self.x += self.speed * dt
        self.rect.x = self.x

    '''Method called every tick to move the objects.'''
    def update(self,dt):
        self.move(dt)

    '''Draws the object to the screen.'''
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)