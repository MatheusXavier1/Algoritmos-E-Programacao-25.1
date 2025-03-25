linhas = int(input())
colunas = int(input())

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])
