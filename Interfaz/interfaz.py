from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random


#Crea la ventana principal
raiz = tk.Tk() 
raiz.title("Domino") #Cambiar el nombre de la ventana 
raiz.geometry("900x800") #Configurar tamaño
#-------------------------------------

#Carga la imagen del fondo
ImgMapa = Image.open('fondo.jpeg')
ImgMapa = ImgMapa.resize((905, 805), Image.ANTIALIAS) # Redimension (Alto, Ancho)
ImgMapa = ImageTk.PhotoImage(ImgMapa)
fondo = Label(raiz, image=ImgMapa)
fondo.pack()
fondo.place(x=-5,y=-5)

#Carga la imagen donde van los datos 
comp = Image.open('comp.jpg')
comp = comp.resize((500, 500), Image.ANTIALIAS) # Redimension (Alto, Ancho)
comp = ImageTk.PhotoImage(comp)
mapa = Label(raiz, image=comp)
mapa.pack()
mapa.place(x=200,y=100)
#-------------------------------------

#______________________________________Funciones______________________________________

#---------------------Codigo_de_BackTracking------------------------------------------
etapas = False

def BackTracking(matriz,solucion,fichas,i,j,aux):  #
    global etapas

    #En caso que ya se guardo el numero en vertical con la fila anterior 
    if [i,j] in aux:
        j+=1
        if j>len(matriz):
            j=0
            i+=1
        BackTracking(matriz,solucion,fichas,i,j,aux) 
        return 0

    #Valida si ya se pasaron por todos los datos
    if i>=len(matriz):
        print("La matriz es: ",matriz)
        print("La solucion del algoritmo BackTracking es: ",solucion)
        etapas= True 
        return 0
        
    #En caso que se llegue al final de una fila y no tengo numero a evaluar 
    elif j>len(matriz):
        j=0
        i+=1
        BackTracking(matriz,solucion,fichas,i,j,aux) 
        #No es una solucion, regresa atras y elimina los datos del arreglo solucion y la ficha 
        if solucion[-1]==1:
            j-=1
            aux.pop()
            solucion.pop()
            fichas.pop()    
        return 0

    #Valida que tenga numero a la derecha con el cual hacer la pereja, en caso que no tenga se empareja con el de abajo
    elif j+1>len(matriz):
        
        if i+1>len(matriz)-1:
            return 0
        
        #Ve si la combinacion de la ficha ya se uso antes 
        elif [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i][j],matriz[i+1][j]] in fichas:
            return 0

        #En caso que no este usada se guarda 
        solucion.append(1)
        fichas.append([matriz[i][j],matriz[i+1][j]])
        aux.append([i+1,j])
        j=0
        i+=1
        BackTracking(matriz,solucion,fichas,i,j,aux) 
        #No es una solucion, si la solucion era 1 regresa atras y elimina los datos del arreglo solucion y la ficha
        #Si es 0 solo regresa sin eliminar nada para cambiar el 0 por un 1 y prueba las posibles soluciones para ese dato
        i-=1
        j=len(matriz)
        if solucion[-1]==1:
            aux.pop()
            j-=1
            solucion.pop()        
            fichas.pop()       
        return 0
    #Tiene numero a la derecha para hacer combinacion en horizontal     
    else:
        #Verifica si la combinacion en horizontal ya se uso 
        if [matriz[i][j+1],matriz[i][j]] in fichas or [matriz[i][j],matriz[i][j+1]] in fichas:
            #no puede tener combinacion en vertical ya que está en la ultima fila 
            if i+1>=len(matriz):
                return 0
            #Verifica si la combinacion en vertical ya se uso 
            elif [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i][j],matriz[i+1][j]] in fichas :
                return 0
            #Se guarda la combinacion en vertical 
            else:   
                solucion.append(1)
                fichas.append([matriz[i][j],matriz[i+1][j]])
                aux.append([i+1,j])
                j+=1
                BackTracking(matriz,solucion,fichas,i,j,aux)
                #No es una solucion, si la solucion era 1 regresa atras y elimina los datos del arreglo solucion y la ficha
                #Si es 0 solo regresa sin eliminar nada para cambiar el 0 por un 1 y prueba las posibles soluciones para ese dato
                if solucion[-1]==1:
                    j-=1
                    aux.pop()
                    solucion.pop()
                    fichas.pop()
                return 0

        #Tiene combinacion en horizontal y aun no se usan los dos numeros 
        else:
            #Agrega el 0 a la respuesta así como la ficha para que no se repita adelante 
            #y modifica los indices 
            solucion.append(0)
            fichas.append([matriz[i][j],matriz[i][j+1]])
            j+=2
            BackTracking(matriz,solucion,fichas,i,j,aux)
            
            #En caso que ya se encontro la respuesta 
            if etapas==True:
                return 0

        
            if i+1>=len(matriz):
                if j>len(matriz[0]):
                    j=len(matriz)
                    if i!=0:
                        i-=1    
                j-=2
                solucion.pop()
                fichas.pop()
                return 0
            
            if j>len(matriz[0])-1:
                if solucion[-1]==1:
                    j=len(matriz)
                else:
                    j-=2
            else:    
                j-=2
        
            solucion.pop()
            fichas.pop()

            if [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i][j],matriz[i+1][j]] in fichas :
                return 0

            solucion.append(1)
            fichas.append([matriz[i][j],matriz[i+1][j]])
            aux.append([i+1,j])
            j+=1
            BackTracking(matriz,solucion,fichas,i,j,aux)
            j-=1

            if etapas!=True:
                aux.pop()
                solucion.pop()
                fichas.pop()
            return 0
#---------------------------------------------------------------------

#----------------------Crear_la_matriz--------------------------------
def next_empty(Board, i, j):
    idx = i*len(Board[0]) + j
    for idx in range(i*len(Board[0]) + j, len(Board[0])* len(Board)):
        x = idx//len(Board[0])
        y = idx%len(Board[0])
        if Board[x][y]=='*':
            return (x, y)
    return (-1, -1)

def make_board(x, y):
    return [['*' for x in range(y)] for x in range(x)]

def make_tiles(n):
    Tiles = []
    for x in range(0, n+1):
        for y in range(x, n+1):
            Tiles = Tiles + [[x, y]]
    return Tiles

def check(Board, i, j, ori):
    #Horizontal
    r = False
    if ori==0:
        if j<len(Board[i])-1:
            if Board[i][j]=='*' and  Board[i][j+1]=='*':
                r = True
    #Vertical
    elif ori==1:
         if i<len(Board)-1:
            if Board[i][j]=='*' and Board[i+1][j]=='*':
                r =  True
    return r

def place_tile(Board, i, j, ori, tile):
    Board[i][j] = tile[0]
    if ori == 0:
        Board[i][j+1] = tile[1]
    else:
        Board[i+1][j] = tile[1]

def create_puzzle(n):
    """
    es posible que el algoritmo generador falle y no encuentre un tablero válido
    Si sucede, retorna falso y no genera ningún archivo de salida
    """

    board = make_board(n+1, n+2)
    tiles = make_tiles(n)
    random.shuffle(tiles)
    solution = []

    current_pos = (0, 0)
    while tiles != []:
        next_tile = tiles.pop()
        random.shuffle(next_tile)
        current_pos = next_empty(board, current_pos[0], current_pos[1])
        ori = random.randint(0,1)
        if not(check(board, current_pos[0], current_pos[1], ori)):
            ori = (ori+1)%2
        if check(board, current_pos[0], current_pos[1], ori):
            place_tile(board, current_pos[0],current_pos[1], ori, next_tile)
            solution = solution + [ori]
        else:
            return False

    #Llama la funcion de backtracking y le pasa la matriz como parametro 
    BackTracking(board,[],[],0,0,[])


def toFile(filename, n, board, solution):    
    file = open(filename+ ".txt", "w")
    file.write(str(n) +  "\n")
    file.write("\n")

    #tablero
    for fila in board:
        for e in fila:
            file.write(str(e) + " ")
        file.write("\n")
    file.write("\n")
            
    for i in solution:
        file.write(str(i) + " ")
    file.write("\n")
#_______________________________Crear_la_matriz________________________________________________


def mostrarResultados():
    global etapas
    create_puzzle(9)
    etapas=False

#____________________________Botones y labels__________________________________________________

button1 = tk.Button(raiz, font=("Courier",22), bg="green", text="Start",height=0,width=8,command=mostrarResultados)
button1.place(x=375,y=700)


raiz.mainloop() 
