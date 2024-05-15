#facturizacion de la floreria

#solicitar datos
nombre= input("ingrese tu nombre: ")
correo= input("ingrese su correo: ")
cedula= input("ingrese tu cedula: ")

print("Ingrese el numero de flores para el arreglo")
floresRojas= int(input("Rojas: "))
girasoles= int(input("Girasoles: "))
claveles= int(input("Claveles:"))
dalias= int(input("Dalias: "))

#realizar el proceso
cantidadRojas = floresRojas*0.75
cantidadGirasoles = girasoles*0.5
cantidadCalveles = claveles*1.25
cantidadDalias = dalias*0.95

total = cantidadRojas+cantidadGirasoles+cantidadCalveles+cantidadDalias
pagoConIVA=total+(1.15)

#imprimir resultados
print("----------FACTURA ELECTRONICA-----------")
print(f"Usuario {nombre}")
print(f"El subtotal es de {round(total,2)}") #round sirve para redondear los resultados
print(f"El total es de {round(pagoConIVA,2)}")
print(f"La factura se enviara a su correo electronico: {correo}")
print("-----------MUCHAS GRACIAS---------------")
