import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_registro_clientes():
    while True:
        limpiar_consola()
        print("\n--- Menú de Registro de Clientes ---")
        print("1. Registro Individual")
        print("2. Registro Acompañado")
        print("3. Registro Grupo/Familia")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion.isdigit():
            if opcion == "1":
                limpiar_consola()
                print("\nRegistro Individual en proceso...")
                break
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
        else:
            print("\nPor favor, ingrese un número válido.")
    
