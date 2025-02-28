
Almacenamiento = {"nombres": [], "numeros": [], "direcciones": []}

def MenuPrincipal():
    print(f"\nQuerido/a {name}, Nuestra lista de movimientos son los siguientes \n 1- Registro de datos \n 2- Búsqueda de datos \n 3- Listado de clientes \n 4- eliminción de datos  \n 5- salir \n ")

def RetiradaDeEmergencia():
    BackMenu = input("\n¿Quieres regresar al menú principal? Responde con 'sí' o 'no' : \n").lower()
    if BackMenu == "si":
        MenuPrincipal()
    elif BackMenu == "no":
        Exit = (input("\n¿quieres salir del programa? Responde con 'si' o 'no' : \n")).lower()
        if Exit == "si":
            print("\nElige la opción 5 para salir \n")
        elif Exit == "no":
            BackMenu1 = (input("\n¿Quieres volver al menu principal? Responde con 'si' o 'no' : \n")).lower()
            if BackMenu1 == "si":
                MenuPrincipal()
            else:
                print("\nNo podemos realizar tu decisión, espero que comprenda, gracias. \n")

def registro():
    print("\n 1. Nombres \n 2. Numeros \n 3. Direcciones \n 4. Salir :")
    Registration = int(input("Ingresa la categoría de registros : "))
    if Registration == 1:
        print("\n Tu elección es nombres ")
        Names = (input("Introduce el nombre que quieres registrar :")).lower()
        Confirmation1 = (input("Escribe 'confirmo' para enviar el nombre : ")).lower()
        Con1 = Confirmation1.lower()
        if Con1 == "confirmo":
            Almacenamiento["nombres"].append(Names) 
            return None
    elif Registration == 2:
        print("Tu elección es numeros")
        Numbers = int(input("Introduce el numero que quieres registrar : "))
        Confirmation2 = (input("Escribe 'confirmo' para enviar el numero :")).lower()
        if Confirmation2 == "confirmo":
            Almacenamiento["numeros"].append(Numbers)
            return None
    elif Registration == 3:
        print("Tu elección es direcciones")
        Adress = (input("Introduce la dirección que quieres registrar : ")).lower()
        Confirmation3 = (input("Escribe 'confirmo' para enviar la dirección :")).lower()
        Con3 = Confirmation3.lower()
        AdressSpace = Adress + " "
        if Con3 == "confirmo":
            Almacenamiento["direcciones"].append(AdressSpace)
            return None
    elif Registration == 4:
        AgainMenu = (input("¿Volver al menu? responde con si o no : ")).lower()
        if AgainMenu == "si":
            return None
        elif AgainMenu == "no":
            return

def busqueda():
    print("¿Qué quieres buscar?")
    Response = int((input("\n 1. Nombre \n 2. Numeros \n 3. Direcciones \n 4. Salir : ")))
    if Response == 1:
        print("Tu elección es busqueda de nombres \n")
        SearchName = input("Introduce el nombre que deseas buscar : ").lower()
        if SearchName in Almacenamiento["nombres"]:
            NombreEncontrado = Almacenamiento["nombres"].index(SearchName)
            print(f"El nombre que registraste es {SearchName} y la posición es {NombreEncontrado}")
            return
        else:
            print("No se encontro el nombre ingresado \n")
            return
    elif Response == 2:
        print("Tu elección es busqueda de numeros \n")
        SearchNumber = int(input("Introduce el numero que deseas buscar : "))
        if SearchNumber in Almacenamiento["numeros"]:
            NumeroEncontrado = Almacenamiento["numeros"].index(SearchNumber)
            print(f"El numero que registraste es {SearchNumber} y la posición es {NumeroEncontrado}") 
            return
        else:
            print("No se encontro el numero ingresado \n")
            return
    elif Response == 3:
        print("Tu elección es busqueda de direcciones")
        SearchAdress = input("Introduce la dirección que deseas buscar :").lower()
        if SearchAdress in Almacenamiento["direcciones"]:
            DirecciónEncontrada = Almacenamiento["direcciones"].index(SearchAdress)
            print(f"La dirección que registraste es {SearchAdress} y la posición es {DirecciónEncontrada}")
            return
        else:
            print("No se encontro la dirección ingresada")
            return
    elif Response == 4:
        AgainMenu2 = (input("¿Volver al menu? responde con si o no : ")).lower()
        if AgainMenu2 == "si":
            return None
        elif AgainMenu2 == "no":
            RetiradaDeEmergencia() 

def showData():
    print("\n 1. Nombres \n 2. Números \n 3. Direcciones \n 4. Volver al menú principal")
    option3 = int(input("Ingresa la opción del contenido que quieres ver: "))
    if option3 == 1:
        print("Nombres:", Almacenamiento["nombres"])
    elif option3 == 2:
        print("Números:", Almacenamiento["numeros"])
    elif option3 == 3:
        print("Direcciones:", Almacenamiento["direcciones"])
    elif option3 == 4:
        return None

def DelCliente():
    print("¿Qué quieres eliminar?")
    response = int(input("\n 1. Nombre \n 2. Números \n 3. Direcciones \n 4. Volver al menú principal :"))
    if response == 1:
        print("Tu elección es eliminación de nombres")
        DelName = input("Introduce el nombre que deseas eliminar: ").lower()
        if DelName in Almacenamiento["nombres"]:
            Almacenamiento["nombres"].remove(DelName)
            print(f"El nombre {DelName} ha sido eliminado")
            return 
        else:
            print("No se encontró el nombre ingresado")
            return
    elif response == 2:
        print("Tu elección es eliminación de numeros")
        DelNumber = int(input("Introduce el numero que deseas eliminar: "))
        if DelNumber in Almacenamiento["numeros"]:
            Almacenamiento["numeros"].remove(DelNumber)
            print(f"El número {DelNumber} ha sido eliminado")
            return 
        else: 
            print("No se encontró el número ingresado")
            return
    elif response == 3:
        print("Tu elección es eliminación de direcciones")
        DelAdress = input("Introduce la dirección que deseas eliminar: ").lower()
        if DelAdress in Almacenamiento["direcciones"]:
            Almacenamiento["direcciones"].remove(DelAdress)
            print(f"La dirección {DelAdress} Se elimino.")
            return 
        else:
            print("No se encontró la dirección ingresada")
            return 
    elif response == 4:
        AgainMenu3 = (input("¿Volver al menu? responde con si o no : ")).lower()
        if AgainMenu3 == "si":
            return None
        elif AgainMenu == "no":
            return    

name = input("\nIntroduzca su nombre\n")
print(f"\nBienvenido querid@ {name}\n")

# Muestra Menu Principal 
while True :
    MenuPrincipal()
    Option = int(input("Introduzca su proximo movimiento : "))
    
    # Opción 1. Registrar clientes
    if  Option == 1 :
        while True:
             regSave = registro()
             if regSave is None:
                break
            
        DecisionData1 = (input("\n¿Quieres registrar otro dato?, responde con 'sí' o 'no' : ")).lower()
        if DecisionData1 == "si":
            registro()
        elif DecisionData1 == "no":
            RetiradaDeEmergencia()
    # Opción 2. Buscar clientes
    elif Option == 2:
        while True:
            Search1 = busqueda()
            if Search1 is None:
                 break 
            DecisionData2 = (input("\n¿Quieres Buscar otro dato?, responde con 'sí' o 'no' : ")).lower()
            if DecisionData2 == "si":
                busqueda()
            elif DecisionData2 == "no": 
                RetiradaDeEmergencia()
    # Opción 3. Mostrar lista de clientes
    elif Option == 3:
        while True:
            MostrarDatos = showData()
            if MostrarDatos is None:
                break
            print("\nLista de Clientes Registrados:")
            print("Nombres:", Almacenamiento["nombres"])
            print("Números:", Almacenamiento["numeros"])
            print("Direcciones:", Almacenamiento["direcciones"])
            LookOption1 = input("\n¿Quieres ver otra opción? Responde con 'sí' o 'no': ").lower()
            if LookOption1 == "si":
                showData()
            elif LookOption1 == "no":
                BackMenu3 = input("\n¿Quieres regresar al menú principal? Responde con 'sí' o 'no': ").lower()
                if BackMenu3 == "si":
                    MenuPrincipal()
                elif BackMenu3 == "no":
                    RetiradaDeEmergencia()
    # Opción 4. Eliminar clientes
    elif Option == 4:
        while True: 
            ClienteEliminado = DelCliente()
            if ClienteEliminado is None:
                break
            print(ClienteEliminado)
            LookOption2 = input("\n¿Quieres ver otra opción? Responde con 'sí' o 'no': ").lower()
            if LookOption2 == "si":
                DelCliente()
            else:
                BackMenu4 = input("\n¿Quieres regresar al menú principal? Responde con 'sí' o 'no' : ").lower()
                if BackMenu4 == "si":
                    MenuPrincipal()
                elif BackMenu4 == "no":
                    RetiradaDeEmergencia()
    # Opción 5. Salida del sistema
    elif Option == 5:
        print("Gracias por recurrir a tu sistema de registro de Clientes de confianza, ten un lindo día")
        break




                           
                    