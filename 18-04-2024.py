candidatos = []


def registrar_candidato():
    nombre = input("Nombre y apellidos: ")
    identificacion = input("Identificación: ")
    correo = input("Correo electrónico: ")
    contacto = input("Contacto: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Años de experiencia: "))
    profesion = input("Profesión: ")
    ciudad = input("Ciudad: ")
    sexo = input("Sexo: ")

  
    if 25 <= edad <= 32 and (profesion == "Ing. sistemas" or profesion == "Ing. informatico") and 2 <= experiencia <= 4:
    
        candidato = [nombre, identificacion, correo, contacto, edad, experiencia, profesion, ciudad, sexo]
        candidatos.append(candidato)
        print("Candidato registrado exitosamente.")
    else:
        print("El candidato no cumple con las condiciones para ser registrado.")


def consultar_candidatos():
    if len(candidatos) == 0:
        print("No hay candidatos registrados.")
    else:
        for candidato in candidatos:
            print("Nombre y apellidos:", candidato[0])
            print("Identificación:", candidato[1])
            print("Correo electrónico:", candidato[2])
            print("Contacto:", candidato[3])
            print("Edad:", candidato[4])
            print("Años de experiencia:", candidato[5])
            print("Profesión:", candidato[6])
            print("Ciudad:", candidato[7])
            print("Sexo:", candidato[8])
            print()

while True:
    print("1. Registrar candidato")
    print("2. Consultar candidatos")
    print("3. Salir")
    opcion = input("elegir una : ")

    if opcion == "1":
        registrar_candidato()
    elif opcion == "2":
        consultar_candidatos()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")