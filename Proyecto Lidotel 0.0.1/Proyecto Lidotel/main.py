import os


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_consola()
        print("  ___________________________________________________________ ")
        print(" /                                                           \ ")
        print("|   Sistema de Reservas - Hotel Lidotel Boutique Margarita    |")
        print("|_____________________________________________________________|")
        print("|  _        _   ____      _____    _______   ______   _       |")
        print("| | |      (_) |   _ \   /  _  \  |__   __| |  ____| | |      |")
        print("| | |       _  |  | | | |  | |  |    | |    | |__    | |      |")
        print("| | |      | | |  | | | |  | |  |    | |    |  __|   | |      |")
        print("| | |____  | | |  |_| | |  |_|  |    | |    | |____  | |____  |")
        print("| |______| |_| |_____/   \_____/     |_|    |______| |______| |")
        print("|_____________________________________________________________|")
        print("|            USA LOS NUMEROS PARA MOVERTE EN EL MENU          |")
        print("|                     (1). Nuevo Cliente                      |")
        print("|                     (2). Salir                              |")
        print("|_____________________________________________________________|")

        opcion = input("|Seleccione una opción: ")
        
        if opcion == "1":
            print("No se ha empezado")
            
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            print("\nGracias por usar el sistema de reservas. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

# Ejecutar el menu principal
menu_principal()
