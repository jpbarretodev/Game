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

#gambiarra da atualização de frame
def pass_frame(frames_total: int, start: int):
    """
    Essa função deve ser chamada na main do jogo, pois é um tipo de gambiarra mais evoluída.
    Isso faz com que não tenha mais trabalho no desenvolvimento
    passando assim o módulo de controle de imagens como global e sendo mais fácil
    de modificar. Passe apenas a quantidade de frames da imagem e onde você quer que inicie a próxima contagem.
    """
    global img_imp
    img_imp.frame_img_count += 1
    if img_imp.frame_img_count == frames_total:
        img_imp.frame_img_count = start

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
    control_pers.Interacao.parado(dimensao_tela, pass_frame(9, 2))

    #mostra o conteudo do jogo na tela
    pygame.display.flip()
    relogio.tick(10)

pygame.quit()