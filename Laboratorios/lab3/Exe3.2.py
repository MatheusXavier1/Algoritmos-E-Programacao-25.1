# Receba uma string e depois imprima numa única linha os seguintes itens:

# Número de caracteres, número de letras, número de números, 
# número de símbolos (tudo que não é letras e nem número) e número de palavras.

# Exemplos:

# Input: "Ninguém sabe de nada!"

# Output: 21 17 0 4 4

# Input: "U2 é uma banda formada em 1976"

# Output: 30 19 5 6 7

output=[]

input = str(input("entre seu texto: "))

def QuantosCaracteres (input):
	return (len(input))

output.append(QuantosCaracteres(input))

def QuantasLetras(input):
	letras = 0
	for i in range(len(input)):
		if input[i].isalpha():
			letras += 1
	return letras

output.append(QuantasLetras(input))

def QuantosNumeros(input):
	numeros = 0
	for i in range(len(input)):
		if input[i].isnumeric():
			numeros += 1
	return numeros

output.append(QuantosNumeros(input))

def QuantosSimbolos(input):
	simbolo = 0
	for i in range(len(input)):
		if not  input[i].isalnum():
			simbolo += 1

	return simbolo
output.append(QuantosSimbolos(input))

def QuantasPalavras (input):
	numeroDePalavras = 1
	for j in range(len(input)):

		if input[j]== " ":
			if input[j+1].isalnum():
				numeroDePalavras +=  1
	return numeroDePalavras


output.append(QuantasPalavras(input))

print(output)
