import pygame
import pygame.locals
import img_imp
import control_pers
import persons

#pygame init
pygame.init()
dimensao_tela = pygame.display.set_mode((1280, 720))
relogio = pygame.time.Clock()
running = True

#definindo o personagem principal
persons.Main_person

#contador de frame (para troca de imagem)
img_imp.frame_img_count

#rodando
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #cenario
    dimensao_tela.blit(img_imp.img_bckg, (0, 0))

    #movimentos e interações
    control_pers.interacao(dimensao_tela)

    #mostra o conteudo do jogo na tela
    pygame.display.flip()
    relogio.tick(10)

pygame.quit()