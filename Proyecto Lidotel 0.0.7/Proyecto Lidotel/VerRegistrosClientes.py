import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

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
            print("clientes_individuales")
            input("\nPresione Enter para continuar...")
        elif seleccion == '2':
            print("clientes_acompanados")
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