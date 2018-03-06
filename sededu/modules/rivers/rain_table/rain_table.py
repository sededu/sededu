#python game
#written by jeffrey kwang
#email: jeffskwang@gmail.com
#version = alpha_1

############################
###LIBRARIES###
############################

import pygame
import numpy as np

############################
###PARAMETERS###
############################
#scale of screen_res / DEM_res
scale = 3

#radius of rain cloud
rad = 100

#frame rate
f_rate = 60

############################
###RASTERS###
############################

#load dem
DEM = np.loadtxt('dem.txt',skiprows=6)
res_height,res_width = DEM.shape
min_ele = np.min(DEM[DEM!=-9999])
max_ele = np.max(DEM)
DEM[DEM==-9999] = min_ele

#0|1|2
#3|x|4
#5|6|7
#load direction
DIR = np.loadtxt('DIR.txt',dtype = int, skiprows=6)
DIR[DIR==8] = 5
DIR[DIR==4] = 6
DIR[DIR==2] = 7
DIR[DIR==1] = 4
DIR[DIR==32] = 0
DIR[DIR==64] = 1
DIR[DIR==128] = 2 
DIR[DIR==16] = 3

############################
###PYGAME###
############################

#initialize pygame
x = pygame.init()

#make game display
gameDisplay = pygame.display.set_mode((res_width * scale,res_height * scale))

#set title of game
pygame.display.set_caption('tutorial')

#update screen
pygame.display.update()

#set gameExit to false to enter the main loop
gameExit = False

#set clock for framerate lock
clock = pygame.time.Clock()

############################
###ARRAYS###
############################
game_display_array = np.zeros((res_width,res_height,3),dtype=int)
AREA_old = np.zeros((res_width,res_height),dtype=int)
AREA_new = np.zeros((res_width,res_height),dtype=int)

#setup direction array
direction = np.zeros((res_width,res_height,8),dtype=int)
for i in xrange(0,8):
    direction[:,:,i][np.transpose(DIR)==i] = 1

#coordinate array
coordinates = np.zeros((res_width,res_height,2))
for x_temp in xrange(0,res_width):
    for y_temp in xrange(0,res_height):
        coordinates[x_temp,y_temp,0] = x_temp * scale
        coordinates[x_temp,y_temp,1] = y_temp * scale

############################
###MAIN LOOP###
############################
while not gameExit:
    #event handler (temp event) use pygame events, e.g. contains mouse data, keyboard presses
    for event in pygame.event.get():
        #quit and leave the loop
        if event.type == pygame.QUIT:
            gameExit = True
            
    #mouse location
    if pygame.mouse.get_pressed()[0]:
        (x_mouse,y_mouse) = event.pos
        x_rain = int(x_mouse)
        y_rain = int(y_mouse)
        AREA_old[(coordinates[:,:,0] - x_mouse) ** 2.0 + (coordinates[:,:,1] - y_mouse) ** 2.0 < rad ** 2.0] += 1

    #ROUTE THE RAINFALL
    AREA_new[:-1,:-1] += AREA_old[1:,1:] * direction[1:,1:,0]
    AREA_new[:,:-1] += AREA_old[:,1:] * direction[:,1:,1]
    AREA_new[1:,:-1] += AREA_old[:-1,1:] * direction[:-1,1:,2]
    AREA_new[:-1,:] += AREA_old[1:,:] * direction[1:,:,3]
    AREA_new[1:,:] += AREA_old[:-1,:] * direction[:-1,:,4]
    AREA_new[:-1,1:] += AREA_old[1:,:-1] * direction[1:,:-1,5]
    AREA_new[:,1:] += AREA_old[:,:-1] * direction[:,:-1,6]
    AREA_new[1:,1:] += AREA_old[:-1,:-1] * direction[:-1,:-1,7]

    game_display_array[:,:,0] = (np.transpose(DEM) - min_ele) / (max_ele - min_ele) * 255
    game_display_array[:,:,1] = (np.transpose(DEM) - min_ele) / (max_ele - min_ele) * 255
    game_display_array[:,:,2] = (np.transpose(DEM) - min_ele) / (max_ele - min_ele) * 255
    
    game_display_array[:,:,0][AREA_new > 0] = 255 * (.75 -  0.75 * AREA_new[AREA_new > 0] / (np.max(AREA_new) + 0.01))
    game_display_array[:,:,1][AREA_new > 0] = 255 * (.75 -  0.75 * AREA_new[AREA_new > 0] / (np.max(AREA_new) + 0.01))
    game_display_array[:,:,2][AREA_new > 0] = 255
     
    #DEM surface
    array_to_surface = pygame.surfarray.make_surface(game_display_array)
    surface_scaled = pygame.transform.scale(array_to_surface,(res_width * scale,res_height * scale))
    gameDisplay.blit(surface_scaled,(0,0))


    #update area array
    AREA_old[:,:] = AREA_new[:,:]
    AREA_new[:,:] = 0
    
    #update screen
    pygame.display.update()
    clock.tick(f_rate)      
            

#unintialize and quit pygame
pygame.quit()
quit()
