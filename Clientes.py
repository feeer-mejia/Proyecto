
Almacenamiento = {"nombres": [], "numeros": [], "direcciones": []}

def MenuPrincipal():
    print(f"Querido/a {name}, Nuestra lista de movimientos son los siguientes \n 1- Registro de datos \n 2- Búsqueda de clientes \n 3- Lista de clientes \n 4- extracción de cliente \n 5- salir \n ")

def RetiradaDeEmergencia():
    Decision = input("\n ¿Quieres regresar al menú principal? Responde con 'sí' o 'no' : \n").lower()
    if Decision == "si":
        MenuPrincipal()
    elif Decision == "no":
        Decision1 = (input("\n ¿quieres salir del programa? Responde con 'si' o 'no' : \n"))
        if Decision1 == "si":
            print("\n Elige la opción 5 para salir \n")
        elif Decision1 == "no":
            DecisionN1 = (input("\n ¿Quieres volver al menu principal? Responde con 'si' o 'no' : \n"))
            if DecisionN1 == "si":
                MenuPrincipal()
            else:
                print("\n No podemos realizar tu decisión, espero que comprenda, gracias \n")


def registro():
    print("\n 1. Nombres \n 2. Numeros \n 3. Direcciones \n 4. Salir :")
    Option2 = (int(input("Ingresa la categoría de registros : ")))
    if Option2 == 1:
        print("\n Tu elección es nombres ")
        Names = (input("Introduce el nombre que quieres registrar :"))
        Confirmation1 = (input("Escribe 'confirmo' para enviar el nombre : "))
        Con1 = Confirmation1.lower()
        if Con1 == "confirmo":
            Almacenamiento["nombres"].append(Names)
            return Names
    elif Option2 == 2:
        print("Tu elección es numeros")
        Numbers = (int(input("Introduce el numero que quieres registrar : ")))
        Confirmation2 = (input("Escribe 'confirmo' para enviar el numero :")).lower()
        if Confirmation2 == "confirmo":
            Almacenamiento["numeros"].append(Numbers)
            return Numbers
    elif Option2 == 3:
        print("Tu elección es direcciones")
        Adress = (input("Introduce la dirección que quieres registrar : "))
        Confirmation3 = (input("Escribe 'confirmo' para enviar la dirección :"))
        Con3 = Confirmation3.lower()
        AdressSpace = Adress + " "
        if Con3 == "confirmo":
            Almacenamiento["direcciones"].append(AdressSpace)
            return AdressSpace
    elif Option2 == 4:
        AgainMenu = (input("¿Volver al menu? responde con si o no : ")).lower()
        if AgainMenu == "si":
            return None
        elif AgainMenu == "no":
            return

def busqueda():
    print("¿Qué quieres buscar?")
    Response = int((input("\n 1. Nombre \n 2. Numeros \n 3. Direcciones \n 4. Salir : ")))
    if Response == 1:
        print("Tu elección es busqueda de nombres")
        SearchNam = input("Introduce el nombre que deseas buscar : ")
        if SearchNam in Almacenamiento["nombres"]:
            NombreEncontrado = Almacenamiento["nombres"].index(SearchNam)
            print(f"El nombre que ingresaste es {SearchNam} y la posición es {NombreEncontrado}")
            return
        else:
            print("No se encontro el nombre ingresado")
            return
    elif Response == 2:
        print("Tu elección es busqueda de numeros")
        SearchNumber = int(input("Introduce el numero que deseas buscar : "))
        if SearchNumber in Almacenamiento["numeros"]:
            NumeroEncontrado = Almacenamiento["numeros"].index(SearchNumber)
            print(f"El numero que ingresaste es {SearchNumber} y la posición es {NumeroEncontrado}") 
            return
        else:
            print("No se encontro el numero ingresado")
            return
    elif Response == 3:
        print("Tu elección es busqueda de direcciones")
        SearchDir = input("Introduce la dirección que deseas buscar :")
        if SearchDir in Almacenamiento["direcciones"]:
            DirecciónEncontrada = Almacenamiento["direcciones"].index(SearchDir)
            print(f"La dirección que ingresaste es {SearchDir} y la posición es {DirecciónEncontrada}")
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

def DelCliente():
    print("¿Qué quieres eliminar?")
    response = int(input("\n 1. Nombre \n 2. Números \n 3. Direcciones \n 4. Volver al menú principal :"))
    if response == 1:
        print("Tu elección es eliminación de nombres")
        DelName = input("Introduce el nombre que deseas eliminar: ")
        if DelName in Almacenamiento["nombres"]:
            Almacenamiento["nombres"].remove(DelName)
            print(f"El nombre {DelName} ha sido eliminado")
            return 
        else:
            print("No se encontró el nombre ingresado")
            return
    elif response == 2:
        print("Tu elección es eliminación de numeros")
        DelNumber = input("Introduce el numero que deseas eliminar: ")
        if DelNumber in Almacenamiento["numeros"]:
            Almacenamiento["numeros"].remove(DelNumber)
            print(f"El número {DelNumber} ha sido eliminado")
            return 
        else:
            return "No se encontró el número ingresado"
    elif response == 3:
        print("Tu elección es eliminación de direcciones")
        DelAdress = input("Introduce la dirección que deseas eliminar: ")
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

name = input("\nintroduzca su nombre\n")
print(f"\nBienvenido querid@ {name}\n")

while True :
    MenuPrincipal()
    Option = (int(input("Introduzca su proximo movimiento : ")))
    
    if  Option == 1 :
        while True:
             regSave = registro()
             if regSave is None:
                break
            
        Decision = (input("\n¿Quieres registrar otro dato?, responde con 'sí' o 'no' : ")).lower()
        if Decision == "si":
            MenuPrincipal()
        elif Decision == "no":
            RetiradaDeEmergencia()
            
    elif Option == 2:
        while True:
            Search1 = busqueda()
            if Search1 is None:
                 break 
            Decision = (input("\n¿Quieres Buscar otro dato?, responde con 'sí' o 'no' : ")).lower()
            if Decision == "si":
                busqueda()
            elif Decision == "no": 
                RetiradaDeEmergencia()
   
    elif Option == 3:
        while True:
            MostrarDatos = showData()
            if MostrarDatos is None:
                break
            print("\nLista de Clientes Registrados:")
            print("Nombres:", Almacenamiento["nombres"])
            print("Números:", Almacenamiento["numeros"])
            print("Direcciones:", Almacenamiento["direcciones"])
            decision = input("\n¿Quieres ver otra opción? Responde con 'sí' o 'no': ").lower()
            if decision == "si":
                showData()
            elif decision == "no":
                Decision = input("\n¿Quieres regresar al menú principal? Responde con 'sí' o 'no': ").lower()
                if Decision == "si":
                    MenuPrincipal()
                elif Decision == "no":
                    RetiradaDeEmergencia()

    elif Option == 4:
        while True: 
            ClienteEliminado = DelCliente()
            if ClienteEliminado is None:
                break
            print(ClienteEliminado)
            decision = input("\n¿Quieres ver otra opción? Responde con 'sí' o 'no': ").lower()
            if decision == "si":
                DelCliente()
            else:
                Decision = input("\n¿Quieres regresar al menú principal? Responde con 'sí' o 'no' : ").lower()
                if Decision == "si":
                    MenuPrincipal()
                elif Decision == "no":
                    RetiradaDeEmergencia()
    elif Option == 5:
        print("Gracias por recurrir a tu registradora de confianza, ten un lindo día")
        break




                           
                    