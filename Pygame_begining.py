import pygame
from random import randrange

''' pygame basic setup '''
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 1

running = True

'''Create a background'''
background = pygame.image.load("bg.jpg").convert()
background = pygame.transform.scale(background, (1280, 720))

'''Create a player'''
player = pygame.image.load('char.png').convert()
player = pygame.transform.scale(player, (100,100))
player_pos_x = screen.get_width()/2
player_pos_y = screen.get_height()/2

'''Create a present'''
present = pygame.image.load('present.jpg').convert()
present = pygame.transform.scale(present, (50,50))

''' looping your frame to run game screen '''
while running:
    # looking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos_y -= 30 * dt
        if keys[pygame.K_s]:
            player_pos_y += 30 * dt
        if keys[pygame.K_a]:
            player_pos_x -= 30 * dt
        if keys[pygame.K_d]:
            player_pos_x += 30 * dt
         
    # fill your screen with the color black to wipe away anything from the last frame
    screen.fill('black')
    # change the backfround image
    screen.blit(background,(0,0))
    
    # render your game
    
    # adding a present object
    screen.blit(present, (900,150))
    
    # moving player
    screen.blit(player, (player_pos_x,player_pos_y))
   
    # get collision event
    player_rec = player.get_rect()
    present_rec = present.get_rect()
    
    
    
    
    # flip display is to put your work on screen
    pygame.display.flip()
    
    clock.tick(60)/1000 # limit the FPS to 60

pygame.display.update()

    
    
