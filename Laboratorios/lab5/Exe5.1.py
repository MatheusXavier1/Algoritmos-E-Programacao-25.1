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

# Matriz A: 2x3
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matriz B: 2x2
B = [
    [7, 8],
    [9, 10]
]


def MultiplicacaoDeMatrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return False
    else:
        return True
print(MultiplicacaoDeMatrizes(A,B))