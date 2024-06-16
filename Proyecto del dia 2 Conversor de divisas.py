import datetime

# Nombre del usuario
nombre = input("Ingrese su nombre por favor: ")

# BIENVENIDA
fecha_y_hora = datetime.datetime.now().strftime("%d/%B/%Y a las %H:%M:%S")
print(f"El programa de cambio de divisas RMD le da la bienvenida sr/sra {nombre} y le informa que la fecha en la que está realizando su operación es: {fecha_y_hora}")

#Dólares
dollar = float(input("Porfavor ingrese la cantidad de dólares a intercambiar: "))


def conversor_euros(dolares):
    #Intercambio a euros
    euros = dollar*(0.88)

    #Repatir billetes y monedas
    billetes_10 = int(euros//10)
    print(f"Estimado usuario {nombre}, se le entregará {billetes_10} billetes de 10 euros", end="")


    billetes_1 = int(euros % 10) #aqui tambien se puede hacer
    #restante = euros % 10
    #billetes_1 = int(restante // 1)

    print(f", {billetes_1} billetes de 1 euro", end="")

    #Aqui se puede hacer
    # monedas = int((restante - billetes_1) * 100) 
    monedas = int(((euros % 10) % billetes_1)*100)
    print(f" y {monedas} monedas de 1 céntimo.")
    return None

cambio = conversor_euros(dollar)