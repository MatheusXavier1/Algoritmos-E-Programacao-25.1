# Ler duas matrizes (todos os elementos são inteiros)

# Faça uma função que retornar a multiplicação dessas duas matrizes.

# Caso a multiplicação não seja válida imprimir 'Erro!'

# Exemplo

# input: [[2,1],[3, 2]] [[1,2],[1,1]] Output:[[3,5],[5,8]]

# input:[[1]] [[2]] Output: [[2]]

# input: [[1,2]] [[1],[2]] Output: [[5]]

# input:[[1],[2]] [[1,2]] Output: [[1,2],[2,4]]

# input:[[1,0],[0,0]] [[2]] Output: Erro!

# obs: Faça duas leituras, uma para cada matriz

A = eval(input())
B = eval(input())

def MultiplicacaoDeMatrizes(matrizA, matrizB):
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    linhasB = len(matrizB)
    colunasB = len(matrizB[0])

    if colunasA != linhasB:
        return ValueError("Matriz Invalida")

    resultado = [[0 for _ in range(colunasB)] for _ in range(linhasA)]

    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA):
                print(A[i][k], "*", B[k][j])
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

print(MultiplicacaoDeMatrizes(A,B))    

