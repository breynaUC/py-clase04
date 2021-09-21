#LISTA
lista = [1,2,3]
#TUPLAS
tupla = ("Java", True, "Yanet", 10, 10.7, False, 10, [5,7,9])
print(tupla)
print(tuple(lista))
print(tupla[1])
#ITERAR UNA LISTA
for i in tupla:
    print(i)
#count()
print(tupla.count(10))
#index()
print(tupla.index("Yanet"))
#len
print(len(tupla))