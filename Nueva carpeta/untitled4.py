


import webbrowser

print ("bienvenido ")
dia = input("ingrese un día de la semana: ")

match (dia):
    case "lunes":
         print("Hoy debes, hacer ejercicios")
     case "martes":
         print("hoy debes, hacer las compras")
     case "miercoles":
         print("Hoy debes, hacer ver peliculas")
     case "jueves":
         print("hoy debes, hacer deberes")
     case "viernes":
         print("Hoy debes, jugar futbol")
     case _:
         print("No existe actividad para ese día")     