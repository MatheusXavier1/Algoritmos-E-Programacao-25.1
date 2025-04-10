#Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.

#Dizemos que uma matriz quadrada de inteiros é um quadrado mágico se a soma dos elementos
# de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.

a =    [[2,3,4],
	[5,6,4],
	[5,6,4]]

def VerificaQuadradoMagico(matriz):
	valoresLinhas = []
	for l in range(len(matriz)):
		somaLinhas = 0
		for c in range(len(matriz[0])):
			somaLinhas+= matriz[l][c]
		valoresLinhas.append(somaLinhas)
	#verificando se todos os valores sao iguais
	valoresLinhas.sort()
	delta = valoresLinhas[-1] - valoresLinhas[0]

	if delta == 0:
		print("todos iguais")
	else:
		print("tem diferente")

print(VerificaQuadradoMagico(a))
