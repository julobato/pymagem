# -*- coding: utf-8 -*-

class Pymagem:

    def __init__(self, nlins, ncols, valor=0):
        self.pymagem = []*nlins
        for j in range(ncols):
            self.pymagem.append([valor]*ncols)
        self.nlins = nlins
        self.ncols = ncols

        
        
    #--------------------------------------------------------------- 
        
    def __str__(self):

       str = ""
       for i in range(0,self.nlins,1):
           for j in range(0, self.ncols,1):
               valor = "%s"%(self.pymagem[i][j])
               str = str + valor 
               a = self.ncols-1
               if j != a:
                   str = str + ", "
           str = str + "\n"    
       return(str)        
    
    def __add__(self,other):

        if self.nlins != other.nlins:
            return ("As imgens não possuem mesmo tamanho\n")
        if self.ncols != other.ncols:
            return ("As imagens não possuem mesmo tamanho\n")
        nova = Pymagem(self.nlins,self.ncols)
        for i in range(0,self.nlins,1):
            for j in range(0,self.ncols,1):
                nova.pymagem[i][j] = self.pymagem[i][j]+other.pymagem[i][j]
        return nova
                
    def __mul__(self,alfa):
        nova = Pymagem(self.nlins,self.ncols)
        for i in range(0,self.nlins,1):
            for j in range(0,self.ncols,1):
                nova.pymagem[i][j] = float(self.pymagem[i][j]*alfa)
        return nova
    
    def pinte_retangulo(self,tlin,tcol,blin,bcol,valor):
        retangulo = Pymagem(blin-tlin, bcol-tcol, valor)
        self.paste(retangulo,tlin,tcol)
    
    def pinte_disco(self,lin,col,raio,val):
        for i in range(0,self.nlins):
            for j in range(0,self.ncols):
                if (i-lin)**2+(j-col)**2 < raio**2:
                    self.put(i,j,val)
                    
    def clone_imagem(self):
        img = Pymagem(self.nlins, self.ncols)
        for i in range(0, self.nlins):
            for j in range(0, self.ncols):
                img.pymagem[i][j] = self.pymagem[i][j]
        return img
        
    def paste(self, other, tlin, tcol):
        slin = self.nlins-1
        scol = self.ncols-1
        olin = other.nlins-1
        ocol = other.ncols-1
        contlin, contcol=0,0
        if tlin >= 0 : 
            if slin-tlin >= olin: 
                lins = tlin + other.nlins
            else:
                lins = self.nlins
        if tcol >= 0 : 
            if scol-tcol >= ocol: 
                cols = other.ncols + tcol
            else:
                cols = self.ncols
        if tlin < 0:
            contlin = 0 - tlin                       
            lins = olin + 1+ tlin
            if slin-tlin >= olin: 
                lins = self.nlins
        if tlin < 0 :
            tlin = 0
        if tcol < 0:
            contcol = 0 - tcol                       
            cols = ocol + 1 + tcol 
            if scol-tcol >= ocol: 
                cols = self.ncols
        if tcol < 0:
            tcol = 0
        
        for i in range(tlin,lins):
            for j in range(tcol, cols):
                self.pymagem[i][j] = other.pymagem[contlin][contcol]
                contcol = contcol + 1
            contlin = contlin + 1
            contlin = 0
            contcol = 0
        
    def size(self):
        lins = self.nlins
        cols = self.ncols
        return(lins, cols)

    def crop(self, tlx=0, tly=0, brx=0, bry=0):
        if tlx == 0 and tly == 0 and brx == 0 and bry == 0:
            img = self.clone_imagem()
            return img
        imagem = Pymagem(brx-tlx, bry-tly)
        for i in range(tlx, brx):
            for j in range(tly, bry):
                valor = self.get(i,j)
                imagem.put(i-tlx,j-tly,valor)
        return imagem

    def get(self, lin, col):
        matriz = self.pymagem[lin]
        valor = matriz[col]
        return valor
        
    def put(self, lin, col, valor):
        self.pymagem[lin][col] = valor

    def get_mat(self):
        return self.pymagem