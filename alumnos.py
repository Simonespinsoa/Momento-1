def registrar_ingreso(alumnos):
    nombre = input('Nombre del alumno: ').strip()
    if not nombre:
        print("Nombre no válido.")
        return
    if nombre in alumnos:
        print(f"{nombre} ya está registrado.")
    else:
        alumnos[nombre] = []
        print(f"{nombre} registrado correctamente.")

def registrar_nota(alumnos):
    nombre = input("Alumno: ").strip()
    if nombre not in alumnos:
        print("Alumno no encontrado. Te recomiendo registrarte primero.")
        return
    try:
        nota = float(input("Nota (0-5): "))
    except ValueError:
        print("Nota inválida.")
        return
    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5.")
        return
    alumnos[nombre].append(nota)
    print(f"{nota} agregada a {nombre}")

def ver_promedio(alumnos):
    nombre = input("Alumno: ").strip()
    if nombre not in alumnos:
        print("Alumno no encontrado.")
        return
    notas = alumnos[nombre]
    if not notas:
        print(f"{nombre} no tiene notas registradas.")
        return
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

def listar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    for nombre, notas in alumnos.items():
        prom = sum(notas) / len(notas) if notas else None
        notas_str = ", ".join(map(str, notas)) if notas else "sin notas"
        print(f"- {nombre}: {notas_str}" + (f" -> prom: {prom:.2f}" if prom is not None else ""))

def menu():
    alumnos = {}
    while True:
        print("\nMenú:")
        print("1. Registrar ingreso")
        print("2. Registrar nota")
        print("3. Ver promedio")
        print("4. Listar alumnos")
        print("5. Salir")
        opcion = input("Opción (1-5): ").strip()
        if opcion == "1":
            registrar_ingreso(alumnos)
        elif opcion == "2":
            registrar_nota(alumnos)
        elif opcion == "3":
            ver_promedio(alumnos)
        elif opcion == "4":
            listar_alumnos(alumnos)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
