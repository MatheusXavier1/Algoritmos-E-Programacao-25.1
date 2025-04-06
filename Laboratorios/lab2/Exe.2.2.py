v1 = eval(input())
v2 = eval(input())

j,flag = 0,0

for elemento in v1:
    while j<len(v2):
        if elemento == v2[j] and type(elemento) == type(v2[j]):
            print(elemento)
            print(v2[j])
            flag+=1
            break
        j+=1    
print(flag == len(v1))