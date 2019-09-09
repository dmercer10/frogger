
'''Board Settings'''
width = 700
size = (width,width)
numRows = 15
numWaterRows = 6
numTrafficRows = 6
spacing_constant = 0
bg_color = (0,0,0)

'''Constants that don't need to be manually changed'''
square_constant = width/numRows
obstacle_height = square_constant - spacing_constant

'''Time it takes to loose the game'''
time = 40000

'''Frog settings'''
frog_color = (50,250,50)
frog_size = square_constant - spacing_constant
frog_lives = 3

'''Truck settings'''
truck_speed = 65
truck_width = 100
truck_color = (100,0,100)
truck_freq = 0.48

'''Car settings'''
car_speed = 85
car_width = 50
car_color = (0,0,100)
car_freq = 0.4

'''Fast Car settings'''
fast_car_speed = 135
fast_car_width = 40
fast_car_color = (100,100,100)
fast_car_freq = 0.35

'''Tractor settings'''
tractor_speed = 60
tractor_width = 80
tractor_color = (200,200,200)
tractor_freq = 0.48

'''Turtle settings'''
turtle_speed = 65
turtle_width = square_constant
turtle_color = (0,100,0)
turtle_freq = 0.5

'''Log settings'''
log_speed = 90
log_width = 60
log_color = (164,42,42)
log_freq = 0.5