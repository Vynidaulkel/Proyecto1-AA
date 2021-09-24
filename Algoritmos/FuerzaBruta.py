
def FuerzaBruta(matriz, n):
    arregloSolucion = []
    posibilidades = [[]]*n
    CrearPermutaciones(posibilidades, n, arregloSolucion)
    print(arregloSolucion)

def CrearPermutaciones(A,n, pArregloSolucion):
    if n==0:
        #print(A) #cambiar a que retorne un arreglo ([[pos1],[pos2]])
        b = A.copy()
        print(A)
        pArregloSolucion.append(b)
    else:
        A[n-1] = 0
        CrearPermutaciones(A, n-1, pArregloSolucion)
        A[n-1] = 1
        CrearPermutaciones(A, n-1, pArregloSolucion)

def busqueda():
    return