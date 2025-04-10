#Ler duas matrizes (todos os elementos são inteiros) Am×n e Bm×n
#. obs: Faça duas leituras, uma para cada matriz

#Fazer uma função que retornar a soma das matrizes, ou seja, A+B. Caso a soma não seja válida imprimir 'Erro!'

#Imprima o retorna da função. A matriz resultante ou a mensagem de erro.

#obs: número de colunas e/ou número de linhas pode ser 1. 


matrizA = eval(input())
matrizB = eval(input())

def SomaDeMatrizes(matrizA, matrizB):

	if len(matrizA) != len(matrizB): 
		return "Erro!"

	matrizC = []
	for i in range(len(matrizA)):
		matrizC.append([])

	for  l in range(len(matrizA)):
		for c in range(len(matrizA[0])):
			matrizC[l].append((matrizA[l][c] + matrizB[l][c]))
	return matrizC
print(SomaDeMatrizes(matrizA,matrizB))
