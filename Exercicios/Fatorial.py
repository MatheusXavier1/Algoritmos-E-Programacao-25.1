def fatorial(numero):
    if numero == 0:
        return 1
    for x in range(numero):
        if x != 0:
		 numero *= x
    return numero
    
print(fatorial(6))
