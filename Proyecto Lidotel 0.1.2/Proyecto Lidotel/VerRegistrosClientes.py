import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def gestionar_registro(archivo):
    while True:
        limpiar_consola()
        print(" ______________________________________ ")
        print(f"|  GESTIÓN DE {archivo.upper()}  |")
        print("| (1). Ver registros                   |")
        print("| (2). Buscar un cliente               |")
        print("| (3). Modificar un registro           |")
        print("| (4). Volver al menú anterior         |")
        print("|______________________________________|")
        seleccion = input("|Ingrese una opción: ")

        if seleccion == '1':
            ver_registros(archivo)
        elif seleccion == '2':
            buscar_cliente(archivo)
        elif seleccion == '3':
            modificar_datos_cliente(archivo)
        elif seleccion == '4':
            break  
        else:
            print("|Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

def ver_registros(archivo):
    try:
        with open(archivo, "r") as file:
            registros = file.readlines()
            if registros:
                limpiar_consola()
                print("\n|--- LISTADO DE REGISTROS ---|")
                for i, registro in enumerate(registros, 1):
                    print(f"| Registro {i}: {registro.strip()}")
                    input("|Presione Enter para ver el siguiente... ")
                print("|Fin de los registros.")
            else:
                print("|No hay registros en este archivo.")
    except FileNotFoundError:
        print("|No hay registros aún.")


def buscar_cliente(archivo):
    cedula_buscar = input("|Ingrese la cédula o nombre del cliente a buscar: ")
    try:
        with open(archivo, "r") as file:
            registros = file.readlines()
            for registro in registros:
                if cedula_buscar in registro:
                    print(f"|Cliente encontrado: {registro.strip()}")
                    input("\nPresione Enter para continuar...")
                    return
        print("|Cliente no encontrado.")
    except FileNotFoundError:
        print("|No hay registros aún.")
    input("\nPresione Enter para continuar...")

def modificar_datos_cliente(archivo):
    cedula_modificar = input("|Ingrese la cédula del cliente a modificar: ")
    try:
        with open(archivo, "r") as file:
            registros = file.readlines()

        for i, registro in enumerate(registros):
            datos = registro.strip().split(",")
            if datos[2] == cedula_modificar:
                print(f"|Cliente encontrado: {registro.strip()}")
                print("|¿Qué datos desea modificar?")
                print("|1. Nombre")
                print("|2. Apellido")
                print("|3. Email")
                print("|4. Teléfono")
                print("|5. Días de estadía")
                opcion_modificar = input("|Ingrese el número de la opción: ")

                if opcion_modificar == '1':
                    datos[0] = input("|Ingrese el nuevo nombre: ")
                elif opcion_modificar == '2':
                    datos[1] = input("|Ingrese el nuevo apellido: ")
                elif opcion_modificar == '3':
                    datos[3] = input("|Ingrese el nuevo email: ")
                elif opcion_modificar == '4':
                    datos[4] = input("|Ingrese el nuevo teléfono: ")
                elif opcion_modificar == '5':
                    datos[5] = input("|Ingrese los nuevos días de estadía: ")
                else:
                    print("|Opción no válida.")
                    return

                registros[i] = ",".join(datos) + "\n"
                with open(archivo, "w") as file:
                    file.writelines(registros)
                print("|Datos modificados correctamente.")
                input("\nPresione Enter para continuar...")
                return
        print("|Cliente no encontrado.")
    except FileNotFoundError:
        print("|No hay registros aún.")
    input("\nPresione Enter para continuar...")


def menu_ver_modificar_registros():
    while True:
        limpiar_consola()
        print(" ______________________________________ ")
        print("|         VER/MODIFICAR REGISTROS      |")
        print("|______________________________________|")
        print("| (1). Registros Individuales          |")
        print("| (2). Registros Acompañado            |")
        print("| (3). Registros Grupo/Familia         |")
        print("| (4). Volver al menú principal        |")
        print("|______________________________________|")
        seleccion = input("|Ingrese una opción: ")

        if seleccion == '1':
            gestionar_registro("clientes_individuales.txt")
            input("\nPresione Enter para continuar...")
        elif seleccion == '2':
            gestionar_registro("clientes_acompanados.txt")
            input("\nPresione Enter para continuar...")
        elif seleccion == '3':
            print("clientes_grupo_familia")
            input("\nPresione Enter para continuar...")
        elif seleccion == '4':
            print("|Volviendo al menú principal...")
            break 
        else:
            print("|Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")