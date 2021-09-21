estudiantes= {"Raul":21,"Jairo":18,"Keyla":19}
nombre = input("Nombre: ")
if nombre.title() in estudiantes:
    print(estudiantes[nombre.title()])
else:
    print("No existe")