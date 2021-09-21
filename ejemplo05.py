personas={}
n = int(input())
for i in range(n):#numero que se van ha solicitar los datos n=3
    nombre = input("Nombre: ")
    fecha = input("Fecha Nac.:")
    personas[nombre]=fecha
print(personas)
