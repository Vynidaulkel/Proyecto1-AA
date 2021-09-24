def FuerzaBruta(matriz, n):
    arregloSolucion = []
    cant = (((n+2)*(n+1))//2)
    posibilidades = [[]]* cant
    CrearPermutaciones(posibilidades, cant, arregloSolucion)
    busqueda(matriz, arregloSolucion)

def CrearPermutaciones(A,n, pArregloSolucion):
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
    #arregloSolucion son TODAS las soluciones
    #n es UNA solucion
    rowsMatriz = len(matriz) -1
    colsMatriz = len(matriz[0]) -1
    for n in arregloSolucion:
        funciona = True
        row = 0
        col = 0
        fichas = []
        fichasVerticales = []

        for i in n:
            print((i), row, col)
            #cuando row es 3 da error
            while [row,col] in fichasVerticales:
                if col + 1 > colsMatriz:
                    row+=1
                    col = 0
                else: 
                    col+=1
            print(i, row, col)

            if i == 0: 
                if col+1 <= colsMatriz:
                    if [matriz[row][col], matriz[row][col+1]] in fichas:
                        funciona = False
                        print("Solucion no funcional: " + str(n))
                        break 
                    fichas.append([matriz[row][col], matriz[row][col+1]])
                    fichas.append([matriz[row][col+1],matriz[row][col]])
                    if col +2 > colsMatriz:
                        row+=1
                        col=0
                    else:
                        col+=2
                else:
                    funciona = False
                    print("Solucion no funcional: " + str(n))
                    break 

            elif i == 1:
           
                if row+1 <= rowsMatriz:
                    #revisa si la ficha ya esta repetida o no
                    if [matriz[row][col], matriz[row+1][col]] in fichas:
                        funciona = False
                        print("Solucion no funcional: " + str(n))
                        break 
                    fichas.append([matriz[row][col], matriz[row+1][col]])
                    fichas.append([matriz[row+1][col],matriz[row][col]])
                    fichasVerticales.append([row+1,col])

                    if col+1 > colsMatriz:
                        col=0
                        if row + 1 > rowsMatriz:
                            funciona = False
                            print("Solucion no funcional: " + str(n))
                            break 
                        else:
                            row+=1
                    else:
                        col+=1
        if funciona == True:
            print("La solucion es: " + str(n))
            break
    return

