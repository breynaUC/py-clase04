diccionario = {"el":"the","grande":"big","es":"is","perro":"dog","bueno":"good","yo":"i","tengo":"have"}
frase = input('Frase: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')