import pygame
import img_imp
import persons

gravidade = 3

def pass_frame(frames_total: int, start: int):
    """
    Passe apenas a quantidade de frames da imagem e onde você quer que inicie a próxima contagem.
    """
    global img_imp
    img_imp.frame_img_count += 1
    if img_imp.frame_img_count == frames_total:
        img_imp.frame_img_count = start

def interacao(dimensao_tela):
        if pygame.key.get_pressed()[pygame.K_d]:
            persons.Main_person.x_pos += persons.Main_person.velocidade
            dimensao_tela.blit(img_imp.Img_pers.img_walk, (persons.Main_person.x_pos, persons.Main_person.y_pos), (img_imp.frame_img_count*128, 0, 128, 128))
            pass_frame(10, 0)
        else:
            dimensao_tela.blit(img_imp.Img_pers.img_idle, (persons.Main_person.x_pos, persons.Main_person.y_pos), (img_imp.frame_img_count*128, 0, 128, 128))
            pass_frame(9, 2)