#Definir el nuemro de contactos inicial 

agenda_inicial_Maria = {"Jose": 987867321, "Raul": 7654321234, "Pablo": 9087654321}
agenda_inicial_Josefina = {"Carlos": 9032415432, "David": 7654321234, "Luis": 908765432}
agenda_general = {"Maria": agenda_inicial_Maria, "Josefina": agenda_inicial_Josefina}

#Añadir un contacto: Crear un nuevo registro en la agenda (nombre, telefono).
def nuevo_contacto(codigo, agenda_previa):
    num_contactos = int(input("Porfavor escriba el numero de contactos que desea ingresar: "))
    agenda_previa = {}
    for i in range(1,num_contactos+1):
        nombre  = input(f"Ingrese el nombre del contacto {i}: ")
        numero = int(input(f"Ingrese el numero del contacto {i}: "))
        agenda_previa.update({nombre:numero})
    print("La agenda actualizada es: ", agenda_previa)
    return agenda_previa 

#Buscar un contacto: Buscar un contacto por nombre y mostrar su teléfono, o un mensaje de error si no lo encuentra.

def buscar_contacto(codigo, agenda_previa):
    nombre_contacto = input("Ingrese el contacto que busca: ")
    claves = agenda_previa.keys()
    valorcitos = agenda_previa.values()
    if nombre_contacto in claves:
        print(f"El número del contacto {nombre_contacto} es: ",agenda_previa.get(nombre_contacto))
    else:
        print("Ese contacto no es parte de tu agenda.")

#Editar un contacto: Modificar teléfono de un contacto existente.

def editar_contacto(codigo, agenda_previa):
    claves = agenda_previa.keys()
    valorcitos = agenda_previa.values()
    buscado = input("Ingrese el nombre del contacto buscado: ")
    if buscado in agenda_previa:
        cambio = int(input("Ingrese el numero nuevo por el cual desea reemplazar el numero previo de este contacto: "))
        agenda_previa.update({buscado: cambio})
        print(f"La agenda actualizada es: {agenda_previa}")
        return agenda_previa
    else:
        print("Ese contacto no es parte de tu agenda.")

#Eliminar un contacto: Eliminar un contacto de la agenda (investiga los métodos disponibles para lograrlo)

def eliminar_contacto(codigo, agenda_previa):
    eliminar = input("Ingrese el nombre del contacto a eliminar: ")
    if eliminar in agenda_previa:
        agenda_previa.pop(eliminar)
        print(agenda_previa)
    else:
        print("Ese contacto no es parte de tu agenda.")
    return agenda_previa

#Mostrar todos los contactos: Mostrar todos los contactos guardados en la agenda.
def impresion_todos_los_contactos(codigo, agenda_previa):
    agendita = agenda_previa.items()
    print("Su agenda hasta ahora guarda los siguientes contactos: ", agendita) #Quiero que solo se imprima la lista dentro de dict_items

#ACCIONES

registro_usuarios = ["Maria", "Josefina"]

#Aqui empieza el programa 


def acciones(palabra_clave):
    agenda_general = {}
    if ingreso == palabra_clave:
        usuario = input("Ingrese su nombre: ")
        if usuario in registro_usuarios:
            print("Las acciones que se pueden realizar en esta agenda de contactos son: \n 1. Añadir un contacto: Crear un nuevo registro en la agenda (nombre, telefono). \n 2. Buscar un contacto: Buscar un contacto por nombre y mostrar su teléfono, o un mensaje de error si no lo encuentra.\n 3. Editar un contacto: Modificar teléfono de un contacto existente.\n 4.Eliminar un contacto: Eliminar un contacto de la agenda (investiga los métodos disponibles para lograrlo)\n 5.Mostrar todos los contactos: Mostrar todos los contactos guardados en la agenda")
            if usuario == "Maria": 
                navegador = int(input("Ingrese la acción que desea realizar: ")) 
                if navegador == 1:
                    creacion_nuevo_contacto = nuevo_contacto(1, agenda_inicial_Maria)
                elif navegador ==2:
                    busqueda = buscar_contacto(2, agenda_inicial_Maria)
                elif navegador ==3:
                    editar = editar_contacto(3, agenda_inicial_Maria)
                elif navegador ==4:
                    eliminacion_contacto = eliminar_contacto(4, agenda_inicial_Maria)
                elif navegador==5:
                    imprimir_todo = impresion_todos_los_contactos(5,agenda_inicial_Maria)
                else:
                    print("Imprima una acción dentro del rango.")
                    
            elif usuario == "Josefina":
                navegador = int(input("Ingrese la acción que desea realizar: ")) 
                if navegador == 1:
                    creacion_nuevo_contacto = nuevo_contacto(1, agenda_inicial_Josefina)
                elif navegador ==2:
                    busqueda = buscar_contacto(2, agenda_inicial_Josefina)
                elif navegador ==3:
                    editar = editar_contacto(3, agenda_inicial_Josefina)
                elif navegador ==4:
                    eliminacion_contacto = eliminar_contacto(4, agenda_inicial_Josefina)
                elif navegador==5:
                    imprimir_todo = impresion_todos_los_contactos(5,agenda_inicial_Josefina)
                else:
                    print("Imprima una acción dentro del rango.")
        else:
            print("No es usuario de esta base, porfavor retirese.")
    else:
        print("No esta permitido ingresar a esta agenda de diccionarios.")


ingreso = input("Ingrese la palabra clave para iniciar: ")
palabra_clave = "Iniciar"
inicio = acciones(ingreso)