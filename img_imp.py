import pygame
import pygame.locals

#frame image
frame_img_count = 0

#image import
img_bckg = pygame.transform.scale(pygame.image.load("imagens/background.jpg"), (1280, 720))

#Image Person Class
class Img_pers:
    img_att = pygame.image.load("imagens/Gangsters_1/Walk.png")
    img_idle = pygame.image.load("imagens/Gangsters_1/Idle_2.png") #frames: 9
    img_walk = pygame.image.load("imagens/Gangsters_1/Walk.png")
    img_recharge = pygame.image.load("imagens/Gangsters_1/Recharge.png")
    img_jump = pygame.image.load("imagens/Gangsters_1/Jump.png")