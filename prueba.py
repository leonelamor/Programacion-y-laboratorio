from re import S
from sre_constants import CATEGORY_LOC_NOT_WORD
import pygame
import random
gameover=False


#alto y ancho de la ruta
tamaño=ancho , alto =(600,800)
ruta_ancho= int(ancho/1.6)
#marca amarilla
marca_ancho = ancho/80
#inicializo el juego
pygame.init()
ventana = pygame.display.set_mode(tamaño)
pygame.display.set_caption("pruebita")

speed=1
contador=0
linea_derecha= ancho/2+ruta_ancho/4
linea_izquierda=ancho/2-ruta_ancho/4

ventana.fill((60,220,0))

auto=pygame.image.load("auto.png")
auto_pos=auto.get_rect()
auto_pos.center= linea_derecha, alto*0.8

auto2=pygame.image.load("segundoAuto.png")
auto2_pos=auto2.get_rect()
auto2_pos.center = linea_izquierda, alto*0.2

timer=pygame.USEREVENT
pygame.time.set_timer(timer,5000)


pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
sonido_fondo = pygame.mixer.Sound("fondo.mp3")
sonido_fondo.set_volume(0.1)
sonido_fondo.play()




running=True
while running:
    contador+=1
    if contador==1000:
        speed+=0.25
        contador=0
    auto2_pos[1]+=speed
    if auto2_pos[1]>alto:
        auto2_pos[1]= -200
        if random.randint(0,1) == 0:
            auto2_pos.center=linea_derecha,-200
        else:
            auto2_pos.center=linea_izquierda,-200


        

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            running=False
        if evento.type==pygame.KEYDOWN:
            if(auto_pos.x>100):
                if evento.key in [pygame.K_a, pygame.K_LEFT]:
                    auto_pos=auto_pos.move([-(ruta_ancho/2),0])
            if(auto_pos.x<100):         
                if evento.key in [pygame.K_d, pygame.K_RIGHT]:
                    auto_pos=auto_pos.move([(ruta_ancho/2),0])

    pygame.draw.rect(ventana,(50,50,50),(ancho/2-ruta_ancho/2,0,ruta_ancho,alto))

    pygame.draw.rect(ventana,(255,240,60),(ancho/2-marca_ancho/2,0,marca_ancho,alto))

    pygame.draw.rect(ventana,(255,255,255),(ancho/2-ruta_ancho/2+marca_ancho*2,0,marca_ancho,alto))

    pygame.draw.rect(ventana,(255,255,255),(ancho/2+ruta_ancho/2-marca_ancho*3,0,marca_ancho,alto))

    ventana.blit(auto,auto_pos)
    ventana.blit(auto2,auto2_pos)
    if auto_pos[0]== auto2_pos[0] and auto2_pos[1]> auto_pos[1] -250:
    #if auto_pos.collidedict(auto2_pos)
        gameover=True
        sonido_fondo.stop()
        pygame.mixer.music.set_volume(0.4)
        sonido_choque = pygame.mixer.Sound("choque.wav")
        sonido_choque.set_volume(0.05)
        sonido_choque.play()
        if evento.type==timer:
            break

    if(gameover==True):
        ventana.fill((0,0,0))
        font = pygame.font.SysFont("Arial Narrow", 40)
        text = font.render("Game over", True, (255, 0, 0))
        ventana.blit(text,(ancho/2-100,alto/2))



   




        



    pygame.display.flip()
pygame.quit()