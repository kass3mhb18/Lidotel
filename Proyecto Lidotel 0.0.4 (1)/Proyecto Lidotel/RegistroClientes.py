import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def verificar_o_crear_archivo_individual(nombre_archivo_individual):
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo_individual):
        # Si no existe, crear el archivo
        with open(nombre_archivo_individual, "w") as archivo:         
            pass  
    else:
        pass  

# Nombre del archivo a verificar
nombre_del_archivo_individual = "clientes_individuales.txt"


# Función para validar si el campo contiene solo letras
def validar_entrada_alfabetica(entrada):
    return entrada.isalpha()


# Función para validar si el campo contiene solo números
def validar_entrada_numerica(entrada):
    return entrada.isdigit()


def registrar_cliente_individual():
    nombre_del_archivo_individual = "clientes_individuales.txt"

    # Verificar si el archivo de clientes existe antes de iniciar
    verificar_o_crear_archivo_individual(nombre_del_archivo_individual)

    # Pedir datos del cliente
    while True:
        nombre = input("|Nombre: ")
        if not validar_entrada_alfabetica(nombre):
            print("|El nombre solo puede contener letras. Intente de nuevo.")
            continue
        break
    
    while True:
        apellido = input("|Apellido: ")
        if not validar_entrada_alfabetica(apellido):
            print("|El apellido solo puede contener letras. Intente de nuevo.")
            continue
        break
    
    while True:
        cedula = input("|Cédula: ")
        
        # Validar que la cédula solo contenga números
        if not validar_entrada_numerica(cedula):
            print("|Cédula inválida. Debe contener solo números. Intente de nuevo.")
            continue

        # Verificar si la cédula ya está registrada
        with open(nombre_del_archivo_individual, "r") as file:
            registros = file.readlines()
            for registro in registros[1:]:  # Omitir el encabezado
                datos = registro.strip().split(",")
                if len(datos) > 2 and datos[2] == cedula:
                    print("|Error: Ya existe un registro con esta cédula.")
                    break
            else:
                break  # Sale del bucle si no se encontró la cédula
        
    while True:
        email = input("|Email: ")
        if '@' not in email or '.' not in email:
            print("|Email no válido. Intente de nuevo.")
            continue
        break
    
    while True:
        telefono = input("|Teléfono: ")
        if not validar_entrada_numerica(telefono) or len(telefono) < 10:
            print("|Teléfono no válido. Intente de nuevo.")
            continue
        break
    
    while True:
        dias_estadia = input("|Cantidad de días de estadía: ")
        if not dias_estadia.isdigit() or int(dias_estadia) <= 0:
            print("|Días de estadía no válidos. Intente de nuevo.")
            continue
        dias_estadia = int(dias_estadia)
        break
    
    # Guardar los datos en el archivo
    with open(nombre_del_archivo_individual, "a") as file:
        file.write(f"{nombre},{apellido},{cedula},{email},{telefono},{dias_estadia}\n")

    print("\n|Cliente registrado exitosamente.")

    
    

# Menú principal de registro
def menu_registro_clientes():
    # Verificar si el archivo de clientes existe antes de mostrar el menú
    
    # Llamar a la función
    verificar_o_crear_archivo_individual(nombre_del_archivo_individual)

    while True:
        limpiar_consola()
        print(" ______________________________________ ")
        print("| --- Menú de Registro de Clientes --- |")
        print("|______________________________________|")
        print("| (1). Registro Individual             |")
        print("| (2). Registro Acompañado             |")
        print("| (3). Registro Grupo/Familia          |")
        print("| (4). Volver al menú principal        |")
        print("|______________________________________|")
        opcion = input("|Seleccione una opción: ")

        if opcion.isdigit():
            if opcion == "1":
                limpiar_consola()
                registrar_cliente_individual()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                limpiar_consola()
                print("\nRegistro Acompañado en proceso...")
                break
            elif opcion == "3":
                limpiar_consola()
                print("\nRegistro de Grupo/Familia en proceso...")
                break
            elif opcion == "4":
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")
        else:
            print("\nPor favor, ingrese un número válido.")
            input("\nPresione Enter para continuar...")



