import pygame
pygame.init()

window = pygame.display.set_mode((1250, 750))

pygame.display.set_caption("Red Goose Game")

goose_x = 50
goose_y = 50
goose_width = 40
goose_height = 60
goose_vel = 5


running = True

while running:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_a] and goose_x - goose_vel >= 0:
        goose_x -= goose_vel
        
    if keys[pygame.K_d] and goose_x + goose_vel <= 1250 - goose_width:
        goose_x += goose_vel
        
    if keys[pygame.K_w] and goose_y - goose_vel >= 0:
        goose_y -= goose_vel
        
    if keys[pygame.K_s] and goose_y + goose_vel <= 750 - goose_height:
        goose_y += goose_vel
    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (goose_x, goose_y, goose_width, goose_height))
    pygame.display.flip()        
    