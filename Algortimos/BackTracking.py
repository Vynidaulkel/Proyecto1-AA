def BackTracking(matriz,etapa,solucion,fichas,i,j):
    if i>len(matriz)-1:
        print("Estas son las fichas fin de la lsita",fichas)
        print(solucion)
        
    elif j>len(matriz[0])-1:
        print("fin de la linea")
        j=0
        BackTracking(matriz,etapa,solucion,fichas,i+1,j)

    elif j+1< len(matriz[0]):
        if [matriz[i][j],matriz[i][j+1]] in fichas or [matriz[i][j+1],matriz[i][j]] in fichas:
            if [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i+1][j],matriz[i][j]] in fichas:
                print("ya está")
                print(solucion)

            else:
                print("se repitio pero solo 1")
                fichas.append([matriz[i][j],matriz[i+1][j]])
                solucion.append(1)
                j+=1
                BackTracking(matriz,etapa+1,solucion,fichas,i,j) 
        else:
            print("normal")
            fichas.append([matriz[i][j],matriz[i][j+1]])
            solucion.append(0)
            j+=2
            BackTracking(matriz,etapa+1,solucion,fichas,i,j)

           
    elif [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i+1][j],matriz[i][j]] in fichas:
        print("Fin pata tras")
        print(solucion)
        
    else:
        print("tope")
        solucion.append(1)
        fichas.append([matriz[i][j],matriz[i+1][j]])
        j=0
        BackTracking(matriz,etapa+1,solucion,fichas,i+1,j)
