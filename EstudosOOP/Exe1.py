class Conjunto(list):
    def soma_pares(self):
        output = list()
        entrada = set(self)

        for elem in entrada:
            if type(elem) == int and elem > 0:
                output.append(elem)
            elif type(elem) == float and elem.is_integer() and elem > 0:
                output.append(elem)
            elif type(elem) == str:
                try:
                    f = float(elem)
                    if f.is_integer() and f>0:
                        output.append(int(f))
                except:
                    pass
        return sum(el for el in set(output) if el % 2 == 0)
    
c = Conjunto([2, 3, 4, '6', 2.0, 'abc', -4, 6])
print(c.soma_pares())  # 12