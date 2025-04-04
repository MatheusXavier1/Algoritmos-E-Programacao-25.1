alfa = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
text = "abc"
def codec(operation,text,num):
	if operation == True:
		textList = list(text)
		codificado = []
		for char in textList:
			for e in range(len(alfa)):
				if char == alfa[e]:
					codificado.append(alfa[e+num])
		output = ''.join(codificado)
		return output
	else:
		textList = list(text)
		decodificado = []
		for char in textList:
			for e in range(len(alfa)):
				if char == alfa[e]:
					decodificado.append(alfa[e-num])
		output = ''.join(decodificado)
		return output

input = eval(input())

print(codec(input[0],input[1],input[2]))