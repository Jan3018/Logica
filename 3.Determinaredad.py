año_actual = float(input("Escribe año actual"))
año_nacimiento = float(input("Escribe tu año de nacimiento"))


if (año_actual > año_nacimiento):
    print(" ")
else:
    print("Error en los datos")

resta = año_actual - año_nacimiento

print("Fecha de nacimiento " + str(resta))



