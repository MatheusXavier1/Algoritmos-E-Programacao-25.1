# Calcular o determinante de uma matriz quadrada A de tamanho máximo n=3.
# Fazer 3 funções: uma para cada tamanho da matriz.
# Lembrando:
# n=1
# A=[a11] det(A)=a11
# n=2
# det([[a,b],[c,d]])=ad-bc
# n=3
# det([[a,b,c],[d,e,f],[g,h,i]])=(aei+bfg+cdh)-(afh+bdi+ceg)
# Obs: os coeficientes da matriz são inteiros e o formato da matriz é igual ao da aula Lista II


matriz = [
    [2, 5, 3],
    [1, -2, -1],
    [3, 6, 2]
]



def Matriz1X1(matriz):
    return matriz

def Matriz2X2(matriz):
    diagonalPrincipal = 1
    diagonalSecundaria = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                diagonalPrincipal *= matriz[i][j]
            if i != j:
                diagonalSecundaria *= matriz[i][j]
    return diagonalPrincipal-diagonalSecundaria

def Matriz3X3(matriz):
    det3x3 = (matriz[0][0]*matriz[1][1]*matriz[2][2]+
              matriz[0][1]*matriz[1][2]*matriz[2][0]+
              matriz[0][2]*matriz[1][0]*matriz[2][1]-
              matriz[0][2]*matriz[1][1]*matriz[2][0]-
              matriz[1][2]*matriz[2][1]*matriz[0][0]-
              matriz[2][2]*matriz[0][1]*matriz[1][0])
    return det3x3     

print(Matriz3X3(matriz))
