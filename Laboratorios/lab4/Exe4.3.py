#Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.

#Dizemos que uma matriz quadrada de inteiros é um quadrado mágico se a soma dos elementos
# de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
[[8,1,6],
 [3,5,7],
 [4,2,9]]

a = eval(input())


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

def VerificaColunas(matriz):
	a,flag,somaDeColunas,somaColunaUnica = 0,0,0,0
	for j in range(len(matriz)):
		for l in range(len(matriz[0])):
			if flag == 0:
				a+=matriz[l][j]
			somaDeColunas += matriz[l][j]
		flag+=1
	somaColunaUnica = somaDeColunas//len(matriz)

	return somaColunaUnica == a

def VerificaDiagonais(matriz):
	diagonalPrincipal,diagonalSecundaria = 0,0
	for l in range(len(matriz)):
		for j in range(len(matriz[0])):
			if l==j:
				diagonalPrincipal += matriz[l][j]
	
	for l in range(len(matriz)):
		j = len(matriz[0])
		while j != 0:
			j-=1
			diagonalSecundaria += matriz[l][j]
			break

	return diagonalPrincipal == diagonalSecundaria
print(VerificaColunas(a))
print(VerificaDiagonais(a))
print(VerificaLinhas(a))
print(VerificaColunas(a)==VerificaDiagonais(a)==VerificaLinhas(a))