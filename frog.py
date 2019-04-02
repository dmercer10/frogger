from pygame.sprite import Sprite
import pygame
import settings as s

class Frog(Sprite):
    def __init__(self,x,y,size):
        self.spawn = (x,y)
        self.x      = x
        self.y      = y 
        self.size   = size
        self.color  = s.frog_color
        self.rect   = pygame.Rect(self.x,self.y,self.size,self.size)
        self.riding = False
        self.riding_speed = 0
        self.lives = s.frog_lives
        
    def update(self):
        if self.riding:
            self.x += self.riding_speed
            self.rect.x = self.x
        if self.check_death():
            self.respawn()
        if self.y < s.square_constant *(1+s.numWaterRows):
            self.riding = False
            
            
    def respawn(self, landed = False):
        self.x = self.spawn[0]
        self.y = self.spawn[1]
        self.rect.x = self.x
        self.rect.y = self.y
        if not landed: self.lives -= 1
    
    def check_death(self):
        if self.rect.left < 0 or self.rect.top < 0 or self.rect.right > s.width or self.rect.bottom > s.width:
            return True
        return False
    
    def set_riding(self,speed):
        self.riding = True
        self.riding_speed = speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move_up(self):
        if self.rect.top > 0:
            self.y -= s.square_constant
            self.rect.y = self.y
    def move_down(self):
        if self.rect.bottom <= s.width - self.size:
            self.y += s.square_constant
            self.rect.y = self.y
    def move_left(self):
        if self.rect.left > self.size:
            self.x -= s.square_constant
            self.rect.x = self.x
    def move_right(self):
        if self.rect.right < s.width - self.size:
            self.x += s.square_constant
            self.rect.x = self.x