import pygame
import settings as s
from pygame.sprite import Sprite

class LilyPad(Sprite):
    def __init__(self,x,y,width,color):
        super(LilyPad, self).__init__()
        self.taken = False
        self.x =        x
        self.y =        y
        self.width =    width
        self.color =    color
        self.rect =     pygame.Rect(self.x,self.y,self.width,s.obstacle_height)

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)