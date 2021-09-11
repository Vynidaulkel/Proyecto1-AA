from Dominoes import * 



#-------------------------------------------------------------------------------------------------
etapas = False

def BackTracking(matriz,etapa,solucion,fichas,i,j,aux):
    global etapas, Borrado

    #En caso que ya se guardo el numero en vertical con la fila anterior 
    if [i,j] in aux:
        j+=1
        if j>len(matriz):
            j=0
            i+=1
        BackTracking(matriz,etapa,solucion,fichas,i,j,aux) 
        return 0

    #Valida si ya se pasaron por todos los datos
    if i>=len(matriz):
        print(fichas)
        print(solucion)
        etapas= True 
        return 0
        
    #En caso que se llegue al final de una fila y no tengo numero a evaluar 
    elif j>len(matriz):
        j=0
        i+=1
        BackTracking(matriz,etapa,solucion,fichas,i,j,aux) 

        if solucion[-1]==1:
            j-=1
            aux.pop()
            solucion.pop()
            fichas.pop()    
        return 0

    #Valida que tenga numero a la derecha "Tope"
    elif j+1>len(matriz):
        if i+1>len(matriz)-1:
            return 0

        elif [matriz[i+1][j],matriz[i][j]] in fichas or [matriz[i][j],matriz[i+1][j]] in fichas:
            return 0

        solucion.append(1)
        fichas.append([matriz[i][j],matriz[i+1][j]])
        aux.append([i+1,j])
        j=0
        i+=1
        BackTracking(matriz,etapa,solucion,fichas,i,j,aux) 
        i-=1
        j=len(matriz)

        if solucion[-1]==1:
            aux.pop()
            j-=1
            solucion.pop()        
            fichas.pop()       
        return 0
     
    elif etapa!=True:
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
                BackTracking(matriz,etapa,solucion,fichas,i,j,aux)
                
                if solucion[-1]==1:
                    j-=1
                    aux.pop()
                    solucion.pop()
                    fichas.pop()
                return 0
        else:
            solucion.append(0)
            fichas.append([matriz[i][j],matriz[i][j+1]])
            j+=2
            BackTracking(matriz,etapa,solucion,fichas,i,j,aux)
            
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
            BackTracking(matriz,etapa,solucion,fichas,i,j,aux)
            j-=1

            if etapas!=True:
                aux.pop()
                solucion.pop()
                fichas.pop()
            return 0
#-------------------------------------------------------------------------------------------------
