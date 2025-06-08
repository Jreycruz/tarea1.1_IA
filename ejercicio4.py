# Entrada:
# Nombre: Ana | Nota: 90
# Nombre: Luis | Nota: 85
# Nombre: Juan | Nota: 92
# Salida esperada:
# {'Ana': 90, 'Luis': 85, 'Juan': 92}

def registrarEstudiantes():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre == "":
            break
        try:
            nota = int(input(f"Nota de {nombre}: "))
        except ValueError:
            print("Por favor, ingresa una nota válida (número entero).")
            continue
        estudiantes[nombre] = nota

    print("\nDatos almacenados:")
    print(estudiantes)

registrarEstudiantes()
