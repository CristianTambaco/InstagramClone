



PLATO = 10


nombreCliente = input("Ingrese su nombre: ")
numeroPersonas = int(input("Ingrese el numero de personas: "))

if numeroPersonas >= 300:
    costoBanquete = 8.5*numeroPersonas
    print(f"El precio final es {costoBanquete}")

elif numeroPersonas >= 200 and numeroPersonas < 300:
    costoBanquete = 7.5*numeroPersonas
    print(f"el precio final es {costoBanquete}")
else: 
    costoBanquete = PLATO*numeroPersonas
    print(f"el precio final es {costoBanquete}")
