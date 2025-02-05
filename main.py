import pygame
import pygame.locals
import img_imp
import control_pers

#pygame init
pygame.init()
dimensao_tela = pygame.display.set_mode((1280, 720))
relogio = pygame.time.Clock()
running = True

#definindo o personagem principal
class Personagem:
    vida = 100
    velocidade = 5
    x_pos, y_poss = 300, 400
    posicao = (x_pos, y_poss)

#contador de frame (para troca de imagem)
img_imp.frame_img_count

#rodando
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dimensao_tela.blit(img_imp.img_bckg, (0, 0)) #cenario (não mexer por enquanto)
    
    #movimento
    comandos = control_pers.comando()
    if comandos == 1:
        dimensao_tela.blit(img_imp.Img_pers.img_walk, Personagem.posicao, (img_imp.frame_img_count*128, 0, 128, 128))
        
    elif comandos == 0:
        dimensao_tela.blit(img_imp.Img_pers.img_idle, Personagem.posicao, (img_imp.frame_img_count*128, 0, 128, 128))
        
    #mostra o conteudo do jogo na tela
    pygame.display.flip()
    relogio.tick(10)

pygame.quit()