# -*- coding: utf-8 -*-

from pymagem import Pymagem
from pilutil import mostre_animacao
from pilutil import salve_animacao

import random

# Escreva aqui outras constantes que desejar
ALTURA  = 120
LARGURA = 160

BLACK = 0
WHITE = 255
#----------------------------------------------------------------------------
       
def main():
    ''' (None) -> None
    O programa cria um vídeo com 900 Pymagens.
    '''

    random.seed(0)
    surpresa = random.randint(50, 150) # sorteia um tom de cinza  
    cinza = Pymagem(ALTURA, LARGURA, 50)
    branco = Pymagem(ALTURA, LARGURA,WHITE)
    preto = Pymagem(ALTURA,LARGURA,BLACK)
    video = []
    img = cinza.clone_imagem()
#--------------------------------------------------------------------------
    # Gera o escrito "MAC 122":
    
    for i in range(0,50,1):
        img.pinte_retangulo(2,2,10+i,10,0)
        img.pinte_retangulo(2,38,10+i,46,0)
        video.append(img)
        img = img.clone_imagem()
    for i in range(0,65,1):
        if i<55:
            img.pinte_disco(5+i,80-(i*0.3),4,0)
            img.pinte_disco(5+i,80+(i*0.3),4,0)
        if i <33:
            img.pinte_disco(5+i,40-(i*0.4),4,0)
        if i >=33:
            img.pinte_disco(70-i,36.25-(i*0.40),4,0)
        video.append(img)
        img = img.clone_imagem()
    for i in range(0,50,1):
        if i<31:
            img.pinte_disco(5,140-i,4,0)
            img.pinte_disco(58,140-i,4,0)
        img.pinte_disco(5+i,110,4,0)
        video.append(img)
        img = img.clone_imagem()
    for i in range(0,70,1):
        if i < 50:
            img.pinte_retangulo(70,40,70+i,48,0)
        if 0 <= i < 8:
            img.pinte_disco(82-i,55+(i*0.5),4,0)
            img.pinte_disco(82-i,85+(i*0.5),4,0)
        if 8 <= i < 16:
            img.pinte_disco(73,52+i,4,0)
            img.pinte_disco(73,82+i,4,0)
        if 16 <= i < 22:
            img.pinte_disco(60+i,61+(i*0.5),4,0)
            img.pinte_disco(60+i,91+(i*0.5),4,0)
        if 22 <= i < 50 :
            img.pinte_disco(65+i,80-(i*0.4),4,0)
            img.pinte_disco(65+i,110-(i*0.4),4,0)
        if 50 <= i:
            img.pinte_disco(115,8+i,4,0)  
            img.pinte_disco(115,38+i,4,0)
            img.pinte_disco(40,21+i,4,0)
        video.append(img)
        img = img.clone_imagem()
#--------------------------------------------------------------------------
        
    # A imagem e seus elementos mudam de cor: 
    img2 = Pymagem(ALTURA,LARGURA,1)
    img2 = img2*10
    img = img+img2
    video.append(img)
    for i in range(0,90,1):
        for lin in range(0,img.nlins,1):
            for col in range(0,img.ncols,1):
                img.put(lin,col,img.get(lin,col)+i)
        video.append(img)
        img = img.clone_imagem()
    img = branco.clone_imagem()
#--------------------------------------------------------------------------
    
    #Uma bolinha se movimenta pela tela, aumenta e muda de cor:  
    for i in range(0,240,1):
        img.pinte_disco(i*0.5,i*0.25,5,surpresa)
        video.append(img)
        img = branco.clone_imagem()
    for i in range(0,150,1) :
        img.pinte_disco(120-i*0.3,60+i*0.15,5+i*0.8,surpresa-2*i)
        video.append(img)
        img = branco.clone_imagem()
    img = preto.clone_imagem()
    video.append(img)
#--------------------------------------------------------------------------
    
    #Um quadradainho se movimenta pela tela:
    for i in range(0,100,1):
        img.pinte_retangulo(1+i,1,20+i,20,50+i)
        video.append(img)
        img = preto.clone_imagem()
    for i in range(0,100,1):
        img.pinte_retangulo(101-i,1+i,120-i,20+i,150+i)
        video.append(img)
        img= preto.clone_imagem()
        
    salve_animacao(video)
    mostre_animacao(video)



#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()