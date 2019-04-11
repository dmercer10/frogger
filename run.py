import sys, pygame
from pygame.sprite import Group
import settings as s
from frog import Frog
from obstacle import Obstacle
from rowOfObstacles import obstaclesRow as obRow
from lilypad import LilyPad
pygame.init()
myfont = pygame.font.SysFont('lucidaconsole', 50)
pygame.display.set_caption('Frogger')
screen = pygame.display.set_mode(s.size)
row = {x+1:s.square_constant*x for x in range(s.numRows)}
print(row)
frog = Frog(screen.get_rect().centery,s.width-s.square_constant-s.spacing_constant,s.frog_size)
pygame.draw.rect(screen,(0,0,255), pygame.Rect(0,0,s.width,s.square_constant*(s.numWaterRows+1)))

# Traffic Rows
truck_row = obRow(s.truck_width,s.truck_speed,'right',False,s.truck_color,row[13],s.truck_freq)
car_row = obRow(s.car_width,s.car_speed,'left',False,s.car_color,row[14],s.car_freq)
fast_car_row = obRow(s.fast_car_width,s.fast_car_speed,'right',False,s.fast_car_color,row[10],s.fast_car_freq)
car_row2 = obRow(s.car_width,s.car_speed,'left',False,s.car_color,row[11],s.car_freq)
fast_car_row2 = obRow(s.fast_car_width,s.fast_car_speed,'left',False,s.fast_car_color,row[12],s.fast_car_freq)
tractor_row = obRow(s.tractor_width,s.tractor_speed, 'left',False,s.tractor_color,row[9],s.tractor_freq)

traffic = [truck_row,car_row,fast_car_row,car_row2,fast_car_row2,tractor_row]

# Water rows
log_row1 = obRow(s.log_width*4,s.log_speed,'right', True, s.log_color,row[7],s.log_freq)
log_row2 = obRow(s.log_width*3,s.log_speed,'left', True, s.log_color,row[5],s.log_freq)
log_row3 = obRow(s.log_width*5,s.log_speed,'right', True, s.log_color,row[4],s.log_freq)
log_row4 = obRow(s.log_width*3,s.log_speed,'right', True, s.log_color,row[2],s.log_freq)
turtle_row1 = obRow(s.turtle_width*2,s.turtle_speed,'left', True, s.turtle_color,row[6],s.turtle_freq)
turtle_row2 = obRow(s.turtle_width*3,s.turtle_speed,'left', True, s.turtle_color,row[3],s.turtle_freq)

#LilyPads
lilies = [LilyPad(3*x*s.square_constant - 2.4*s.square_constant,0, 1.5*s.square_constant, (100,100,255)) for x in range(1,6)]
lilies_group = Group()
for lily in lilies:
    lilies_group.add(lily)
time = s.time
last_tick = pygame.time.get_ticks()
water = [log_row1,log_row2,log_row3,log_row4,turtle_row1,turtle_row2]

def update_traffic(dt):
    for obj in traffic:
        obj.update(dt)
        
def draw_traffic(screen):
    for obj in traffic:
        obj.draw(screen)
        
def update_water(dt):
    for obj in water:
        obj.update(dt)
        
def draw_water(screen):
    for obj in water:
        obj.draw(screen)
        
def draw_lilies(screen):
    for obj in lilies_group.sprites():
        obj.draw(screen)
        
def check_traffic_collision():
    for obs in traffic:
        if len(pygame.sprite.spritecollide(frog, obs.group,False)) > 0:
            return True
    return False

def check_water_collision():
    return_list = []
    for obs in water:
        return_list += pygame.sprite.spritecollide(frog, obs.group,False)
    return return_list

def check_lily_collision():
    return pygame.sprite.spritecollide(frog, lilies_group , True)


    
clock = pygame.time.Clock()
while frog.lives >0 and time > 0:
    
    dt = clock.tick()
    print(dt)
    
    screen.fill(s.bg_color)
    
    pygame.draw.rect(screen,(0,0,255), pygame.Rect(0,0,s.width,s.square_constant*(s.numWaterRows+1)))
    pygame.draw.rect(screen,(60,60,60), pygame.Rect(0,screen.get_rect().bottom - s.square_constant,s.width,s.square_constant))
    pygame.draw.rect(screen,(60,60,60), pygame.Rect(0,traffic[-1].row - s.square_constant,s.width,s.square_constant))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP:     frog.move_up()
            elif key == pygame.K_DOWN: frog.move_down()
            elif key == pygame.K_LEFT: frog.move_left()
            elif key == pygame.K_RIGHT:frog.move_right()
    
    
    update_traffic(dt)
    draw_traffic(screen)
    update_water(dt)
    draw_water(screen)
    draw_lilies(screen)
    frog.update()
    frog.draw(screen)
    
    
    if check_traffic_collision():
        frog.respawn()
    water_collide = check_water_collision() 
    if len(water_collide) > 0:
        frog.riding = True
        frog.riding_speed = water_collide[0].speed
    elif len(check_lily_collision()) > 0:
        time += s.time
        frog.respawn(True)
    elif frog.y < s.square_constant*(s.numWaterRows+1):
        frog.respawn()
    time -= (pygame.time.get_ticks()-last_tick)
    last_tick = pygame.time.get_ticks()
    
    lives = myfont.render(str(frog.lives), False, (255, 255, 255))
    screen.blit(lives,(screen.get_rect().right-s.square_constant,screen.get_rect().bottom-s.square_constant))
    timer = myfont.render(str(time/1000), False, (255, 255, 255))
    screen.blit(timer,(screen.get_rect().left,screen.get_rect().bottom-s.square_constant))
    
    pygame.display.flip()