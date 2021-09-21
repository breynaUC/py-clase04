simbolos={"Sol":"S","Dolar":"$"}
m = input("M:")
if m.title() in simbolos:
    print(simbolos[m.title()])
else:
    print("no existe")