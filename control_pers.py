import pygame

def comando():
    if pygame.key.get_pressed()[pygame.K_d]:
        return 1
    else:
        return 0
    
def movimento(x_pos):
    x_pos += 10