def MenuPrincipal():
    print(f"Querido {name}, Nuestra lista de movimientos son los siguientes \n 1- Registro de datos \n 2- Busqueda de clientes \n 3- Lista de clientes \n 4- extracción de cliente \n 5- salir \n : ")
    

def registro():
        print("\n 1. Nombres \n 2. Numeros \n 3. Direcciones \n 4. Salir :")
        Option2 = (int(input("Ingresa la categoria de registros")))
        if Option2 == 1:
            print("\n Tu elección es nombres ")
            Names = (input("Intoduce el nombre que quieres registrar :"))
            Confirmation1 = (input("Escribe 'confirmo' para enviar el nombre : "))
            Con1 = Confirmation1.lower()
            if Con1 == "confirmo":
                return Names
            elif Option2 == 2:
                print("Tu elección es numeros")
                Numbers = (int(input("Introduce el numero que quieres registrar : " )))
                Confirmation2 = ((input("Escribe 'confirmo' para enviar el numero :")))
                Con2 = Confirmation2.lower()
                if Con2 == "confirmo":
                    return Numbers
            elif Option2 == 3:
                print("Tu elección es direcciones")
                Adress = (input("Intoduce la dirección que quieres registrar : "))
                Confirmation3 = (input("Escribe 'confirmo' para enviar la dirección :"))
                Con3 = Confirmation3.lower()
                AdressSpace = Adress + " "
                if Con3 == "confirmo":
                    return AdressSpace
            elif Option2 == 4:
                AgainMenu = (input("¿Volver al menu? responde con si o no : ")).lower()
                if AgainMenu == "si":
                    return  None
                elif AgainMenu == "no":
                    return 

def busqueda():
        print("¿Qué quieres buscar?")
        Response = int((input("\n 1. Nombre \n 2. Numeros \n 3. Direcciones \n 4. Salir : ")))
        
        if Response == 1 :
            print("Tu elección es busqueda de nombres")
            SearchNam = input("Introduce el nombre que deseas buscar : ")
            if SearchNam in listNames:
                NombreEncontrado = listNames.index(SearchNam)
                return (f"El nombre que ingresaste es {SearchNam} y la posición es {NombreEncontrado}")
            else:
                ("No se encontro el nombre ingresado")
                return
        elif Response == 2 :
            print("Tu elección es busqueda de numeros")
            SearchNumber = input("Introduce el numero que deseas buscar : ")
            if SearchNumber in listNumbers:
                NumeroEncontrado = listNumbers.index(SearchNumber)
                (f"El numero que ingresaste es {SearchNumber} y la posición es {NumeroEncontrado}") 
                return
            else:
                ("No se encontro el numero ingresado")
                return
        elif Response == 3 :
            print("Tu elección es busqueda de direcciones")
            SearchDir = input("Introduce la dirección que deseas buscar :")
            if SearchDir in listAdress:
                DirecciónEncontrada = (SearchDir)
                (f"El nombre que ingresaste es {SearchDir} y la posición es {DirecciónEncontrada}")
                return
            else:
                ("No se encontro la dirección ingresada")
                return
        elif Response == 4:
            AgainMenu2 = (input("¿Volver al menu? responde con si o no : ")).lower()
            if AgainMenu2 == "si":
                return None
            elif AgainMenu == "no":
                return      
def DelCliente():
    while True:
        print("¿Qué quieres eliminar?")
        response = int(input("\n 1. Nombre \n 2. Números \n 3. Direcciones \n 4. Volver al menú principal :"))
        if response == 1:
            print("Tu elección es eliminación de nombres")
            DelName= input("Introduce el nombre que deseas eliminar: ")
            if DelName in list_names:
                list_names.remove(DelName)
                return f"El nombre {DelName} ha sido eliminado"
            else:
                return "No se encontró el nombre ingresado"
        elif response == 2:
            print("Tu elección es eliminación de numeros")
            DelNumber = input("Introduce el numero que deseas eliminar: ")
            if DelNumber in list_numbers:
                list_numbers.remove(DelNumber)
                return f"El número {DelNumber} ha sido eliminado"
            else:
                return "No se encontró el número ingresado"
        elif response == 3:
            print("Tu elección es eliminación de direcciones")
            DelAdress = input("Introduce la dirección que deseas eliminar: ")
            if DelAdress in list_address:
                list_address.remove(DelAdress)
                return f"La dirección {DelAdress} Se elimino."
            else:
                return "No se encontró la dirección ingresada"
        elif response == 4:
            AgainMenu3 = (input("¿Volver al menu? responde con si o no : ")).lower()
            if AgainMenu3 == "si":
                return None
            elif AgainMenu == "no":
                return    
    


name = (input("\nintroduzca su nombre\n"))
print(f"\nBienvenido querid@ {name}\n")

listNames = []
listNumbers = []
listAdress = []
menuPrin = MenuPrincipal()
while True :
    Menu= MenuPrincipal
    Option = (int(input("Introduzca su proximo movimiento : ")))
    if  Option == 1 :
        while True:
             regSave = registro()
             if regSave is None:
                break
             if type(regSave) == str:
                if " " in regSave:
                    listAdress.append(regSave)
                    print("Introducido correctamente")
             elif type(regSave) == int:
                listNumbers.append(regSave)
                print("Introducido correctamente") 
             elif regSave == "TeacherIrvin":
                break
        Decision = (input("\n¿Quieres registrar otro dato?, responde con 'si' o 'no' : ")).lower()
        if Decision == "si":
            MenuPrincipal()
        elif Decision == "no":
            break
            
    elif Option == 2:
        while True:
            Search1 = busqueda()
            if Search1 is None:
                 break 
            Decision = (input("\n¿Quieres Buscar otro dato?, responde con 'si' o 'no' : ")).lower()
            if Decision == "si":
                busqueda()
            if Decision == "no": 
                break
   
    elif Option == 3:
        while True:
            print("\nLista de Clientes Registrados:")
            print("Nombres:", listNames)
            print("Números:", listNumbers)
            print("Direcciones:", listAdress)
            break
    elif Option == 4:
        while True:
            ClienteEliminado= DelCliente()
            if ClienteEliminado is None:
                break
            print(ClienteEliminado)
            decision = input("\n¿Quieres eliminar otro dato? Responde con 'si' o 'no': ").lower()
            if decision == "no":
                break
    elif Option == 5:
        break

print("Usted añadio :", listNames)
print("Usted añadio :", listNumbers)
print("usted añadio", listAdress)



