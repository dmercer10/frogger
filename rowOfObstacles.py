import pygame
import settings as s
from pygame.sprite import Group
import random
from obstacle import Obstacle

'''Class to be used for each row of a group of moving obstacles.'''
class obstaclesRow(Group):
    def __init__(self,width,speed,direction,jumpable,color,row,frequency):
        self.width =    width
        self.speed =    speed
        self.direction = direction
        self.jumpable = jumpable
        self.color =    color
        self.row = row
        self.frequency = frequency/1000
        self.starting_x = s.width if self.direction == 'left' else -self.width
        self.group = Group()
        self.group.add(Obstacle(s.width if self.direction == 'left' else -self.width,self.row, self.width,self.speed,
                                self.direction, self.jumpable,self.color))

    '''Returns amount of objects in the class'''
    def __len__(self):
        return len(self.group.sprites())


    def check_next_obs_go(self):
        if self.direction == 'left':
            return self.group.sprites()[-1].rect.right + s.square_constant < self.starting_x
        else:
            return self.group.sprites()[-1].rect.left > s.square_constant

    '''Method that updates the entire row of obstacles. This method also adds and removes objects to the row appropriatly.'''
    def update(self,dt):

        '''The if statement is making sure there is objects in the row before calling on their objects.'''
        if len(self.group.sprites()) == 0:
            '''Spawns in new objects just off screen with resonable space between the following object'''
            if random.random() < self.frequency:
                self.group.add(Obstacle(s.width if self.direction == 'left' else -self.width,self.row, self.width,self.speed,
                                    self.direction, self.jumpable,self.color))
        elif self.check_next_obs_go() and random.random() < self.frequency:
            self.group.add(Obstacle(s.width if self.direction == 'left' else -self.width,self.row, self.width,self.speed,
                                self.direction, self.jumpable,self.color))
            

        '''Removes objects in the class that go off the screen'''
        for o in self.group.sprites().copy():
            if o.rect.right < 0 or o.rect.left > s.width:
                self.group.remove(o)
            else:
                o.update(dt)

    '''Draws the entire row of objects to the screen.'''
    def draw(self,screen):
        for o in self.group.sprites():
            o.draw(screen)