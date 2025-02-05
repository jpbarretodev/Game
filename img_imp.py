import pygame
import pygame.locals



#frame image
frame_img_count = 0

#image import
img_bckg = pygame.transform.scale(pygame.image.load("jogo/imagens/background.jpg"), (1280, 720))

#Image Person Class
class Img_pers:
    img_att = pygame.image.load("jogo/imagens/Gangsters_1/Attack_1.png")
    img_idle = pygame.image.load("jogo/imagens/Gangsters_1/Idle_2.png") #frames: 9
    img_walk = pygame.image.load("jogo/imagens/Gangsters_1/Walk.png")