a,b = eval(input()), eval(input())
def TemIguais(lista1, lista2):
    if(len(lista1)==0 or len(lista2)==0): 
        return False
    if(lista1[0] == lista2[0]): 
        return True

    return TemIguais(lista1[1:],lista2[1:])
print(TemIguais(a,b))