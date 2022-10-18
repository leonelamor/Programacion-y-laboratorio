import pygame
import random
ancho=600
alto=600
ancho_flecha=(75,75)
pos_flecha1=(100,500)
# --------------------- CREAR VENTANA ---------------------
pygame.init()
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("pruebita")
ventana.fill((255,0,0))

#-------------------- FONDO -----------------------
fondo=pygame.image.load("img.jpg")
fondo=pygame.transform.scale(fondo,(600,800))

#----------------- FLECHAS ABAJO-----------------
flecha1=pygame.image.load("circuloAzul.png")
flecha2=pygame.image.load("circuloRosa.png")
flecha3=pygame.image.load("circuloRosa.png")
flecha4= pygame.image.load("circuloAzul.png")
flecha1=pygame.transform.scale(flecha1,(ancho_flecha))
flecha2=pygame.transform.scale(flecha2,(ancho_flecha))
flecha3=pygame.transform.scale(flecha3,(ancho_flecha))
flecha4=pygame.transform.scale(flecha4,(ancho_flecha))
# -------------- FLECHAS ABAJO POSICION --------------
flecha1_pos=flecha1.get_rect()
flecha1_pos.center=ancho/6,alto-75

flecha2_pos=flecha2.get_rect()
flecha2_pos.center=ancho/3,alto-75

flecha3_pos=flecha3.get_rect()
flecha3_pos.center=ancho/2,alto-75

flecha4_pos=flecha4.get_rect()
flecha4_pos.center=ancho/1.4,alto-75

#----------------------- FLECHAS HACIA ABAJO ----------------------------

flecha_abajo1=pygame.image.load("circuloAzul.png")
flecha_abajo3=pygame.image.load("circuloRosa.png")
flecha_abajo4= pygame.image.load("circuloAzul.png")
flecha_abajo1=pygame.transform.scale(flecha1,(ancho_flecha))
flecha_abajo3=pygame.transform.scale(flecha3,(ancho_flecha))
flecha_abajo4=pygame.transform.scale(flecha4,(ancho_flecha))

#---------------------- FLECHAS ABAJO POSICION INICIAL ---------------------- 


flecha1_abajo_pos=flecha1.get_rect()
flecha1_abajo_pos.center=ancho/6,75

flecha2_abajo_pos=flecha2.get_rect()
flecha2_abajo_pos.center=ancho/3,75

flecha3_abajo_pos=flecha3.get_rect()
flecha3_abajo_pos.center=ancho/2,75

flecha4_abajo_pos=flecha4.get_rect()
flecha4_abajo_pos.center=ancho/1.4,75

lista_flechas=[]








#------------ BUCLE------------

running=True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running=False

    flecha1_abajo_pos[1]+=2
    flecha2_abajo_pos[1]+=2
    flecha3_abajo_pos[1]+=2
    flecha4_abajo_pos[1]+=2

    if(flecha1_abajo_pos[1]>800):
        flecha1_abajo_pos[1]=-300
    if(flecha1_abajo_pos[1]>800):
        flecha1_abajo_pos[1]=-300
    if(flecha1_abajo_pos[1]>800):
        flecha1_abajo_pos[1]=-300
    if(flecha1_abajo_pos[1]>800):
        flecha1_abajo_pos[1]=-300

    


    flecha_abajo2=pygame.image.load("circuloRosa.png")
    flecha_abajo2=pygame.transform.scale(flecha2,(ancho_flecha))

    ventana.fill((0,0,0))

    ventana.blit(fondo,(0,0))
    ventana.blit(flecha1,flecha1_pos)
    ventana.blit(flecha2,flecha2_pos)
    ventana.blit(flecha3,flecha3_pos)
    ventana.blit(flecha4,flecha4_pos)
    ventana.blit(flecha_abajo1,flecha1_abajo_pos)
    ventana.blit(flecha_abajo2,flecha2_abajo_pos)
    ventana.blit(flecha_abajo3,flecha3_abajo_pos)
    ventana.blit(flecha_abajo4,flecha4_abajo_pos)





    pygame.display.flip()
pygame.display.quit()

