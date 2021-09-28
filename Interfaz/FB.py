def FuerzaBruta(matriz, n): 
    # funcion que crea el arreglo solucion vacio y luego manda a crear todas las posibilidades
    # y por ultimo llama a la funcion que busca solucion
    arregloSolucion = []
    cant = (((n+2)*(n+1))//2)
    posibilidades = [[]]* cant
    CrearPermutaciones(posibilidades, cant, arregloSolucion)
    return busqueda(matriz, arregloSolucion)

def CrearPermutaciones(A,n, pArregloSolucion): 
    #funcion recursivada que crea todas las posibilidades de las soluciones
    if n==0:
        #print(A) #cambiar a que retorne un arreglo ([[pos1],[pos2]])
        b = A.copy()
        pArregloSolucion.append(b)
    else:
        A[n-1] = 0
        CrearPermutaciones(A, n-1, pArregloSolucion)
        A[n-1] = 1
        CrearPermutaciones(A, n-1, pArregloSolucion)

def busqueda(matriz, arregloSolucion):
    #funcion que recorre el arreglo solucion y va probando cada una para ver si funciona
    rowsMatriz = len(matriz) -1   
    colsMatriz = len(matriz[0]) -1  
    for n in arregloSolucion:  
        #resetea valores por cada corrida
        funciona = True
        row = 0
        col = 0
        fichas = []
        fichasVerticales = []

        for i in n:
            #va recorriendo la solucion
            #tiene que revisar si la ficha ya se usó en vertical
            while [row,col] in fichasVerticales:
                if col + 1 > colsMatriz:
                    row+=1
                    col = 0
                else: 
                    col+=1
            #si la solucion es usar una ficha en horizontal
            if i == 0: 
                if col+1 <= colsMatriz:
                    if [matriz[row][col], matriz[row][col+1]] in fichas:
                        funciona = False
                        break
                    #revisa si la ficha ya esta repetida o no
                    fichas.append([matriz[row][col], matriz[row][col+1]])
                    fichas.append([matriz[row][col+1],matriz[row][col]])
                    #suma a la columa o a la fila para ir recorriendo la matriz
                    if col +2 > colsMatriz:
                        row+=1
                        col=0
                    else:
                        col+=2
                else:
                    funciona = False
                    break 

            #si la solucion es usar una ficha en vertical
            elif i == 1:
           
                if row+1 <= rowsMatriz:
                    #revisa si la ficha ya esta repetida o no
                    if [matriz[row][col], matriz[row+1][col]] in fichas:
                        funciona = False
                        break
                    #agrega la ficha al conjunto de fichas usadas
                    fichas.append([matriz[row][col], matriz[row+1][col]])
                    fichas.append([matriz[row+1][col],matriz[row][col]])
                    fichasVerticales.append([row+1,col])
                    #suma a la columa o a la fila para ir recorriendo la matriz
                    if col+1 > colsMatriz:
                        col=0
                        if row + 1 > rowsMatriz:
                            funciona = False
                            break 
                        else:
                            row+=1
                    else:
                        col+=1
        #condicion para revisar si encuentra solucion
        if funciona == True:
            solucion = n
            break    
    return solucion

