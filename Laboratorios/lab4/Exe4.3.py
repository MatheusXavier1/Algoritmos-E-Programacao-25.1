#Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.

#Dizemos que uma matriz quadrada de inteiros é um quadrado mágico se a soma dos elementos
# de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.

a = [[2,3,4],[5,6,4],[5,6,4]]

def VerificaLinhas(matriz):
	somaDeLinhas,a = 0,0
	flag = 0
	for j in  range(len(matriz)):
		for l in range(len(matriz[0])):
			if flag == 0:
				a += matriz[j][l]
			somaDeLinhas += matriz[j][l]
		flag+=1
	somaLinhaUnica = somaDeLinhas//len(matriz)
	return somaLinhaUnica == a

#print(VerificaLinhas(a))

def VerificaColunas(matriz):
	a,flag,somaDeColunas,somaColunaUnica = 0,0,0,0
	for j in range(len(matriz)):
		for l in range(len(matriz[0])):
			if flag == 0:
				a += matriz[j][l]
			somaDeColunas += matriz[j][l]
		flag+=1
	somaColunaUnica = somaDeColunas//len(matriz)

	print(somaDeColunas)
	print(somaColunaUnica)
	print(a)

	return somaColunaUnica == a

print(VerificaColunas(a))
