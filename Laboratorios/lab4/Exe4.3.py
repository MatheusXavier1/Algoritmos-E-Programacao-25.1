#Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.

#Dizemos que uma matriz quadrada de inteiros é um quadrado mágico se a soma dos elementos
# de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.

a = eval(input())

def VerificaQuadradoMagico(matriz):
	valoresLinhas = []
	flag = 0
	for l in range(len(matriz)):
		somaLinhas = 0
		for c in range(len(matriz[0])):
			somaLinhas+= matriz[l][c]
		valoresLinhas.append(somaLinhas)

	valoresLinhas.sort()
	delta1 = valoresLinhas[-1] - valoresLinhas[0]

	if delta1 == 0:
		flag+=1

	valoresColunas = []
	for l in range(len(matriz)):
		somaColunas = 0
		for c in range(len(matriz[0])):
			somaColunas+=matriz[c][l]
		valoresColunas.append(somaColunas)
	valoresColunas.sort()
	delta2 = valoresColunas[-1] - valoresColunas[0]

	if delta2 == 0:
		flag+=1

	valoresDiag = []
	for l in range(len(matriz)):
		for c in range(len(matriz[0])):
			if l==c:
				valoresDiag.append(matriz[l][c])
	for l in range(len(matriz)):
		c = len(matriz[0])-1
		while c >= 0:
			valoresDiag.append(matriz[l][c])
			c-=1
			break
	valoresDiag.sort()
	delta3 = valoresDiag[-1]-valoresDiag[0]
	if delta3 == 0:
		flag+=1

	if flag == 3:
		return True
	return False
print(VerificaQuadradoMagico(a))