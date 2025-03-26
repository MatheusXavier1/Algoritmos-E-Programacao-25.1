# Receba uma string e depois imprima numa única linha os seguintes itens:

# Número de caracteres, número de letras, número de números, 
# número de símbolos (tudo que não é letras e nem número) e número de palavras.

# Exemplos:

# Input: "Ninguém sabe de nada!"

# Output: 21 17 0 4 4

# Input: "U2 é uma banda formada em 1976"

# Output: 30 19 5 6 7
output = []
input = str(input())
espaco, letras, numeros, palavras,simbolo = 0,0,0,0,0
output.append(len(input.lstrip()))

for i in range(len(input)):
    if input[i].isalpha():
        letras+=1

output.append(letras)

for i in range(len(input)):
    if input[i].isnumeric():
        numeros+=1

output.append(numeros)

for i in range(len(input)):
    if input[i].isspace():
        espaco+=1

for i in range(len(input)):
    if not input[i].isalnum():
        simbolo+=1

output.append(simbolo)

palavras = espaco+1
output.append(palavras)

print(output)