cantidadC = float(input("Escribe los °C: "))
cantidadF = float(input("Escribe los °F: "))
cantidadK = float(input("Escribe los K: "))

print("Opciones: \n1.- °C a °F \n2.- °F a °C \n3.- K a °C \n4.- °C a K \n5.- °F a K \n6.- K a °F")

respuesta = int (input("¿Que tipo de convesión quieres realizar?"))

if ( respuesta == 1):
    CaF_F = cantidadC * 1.8 + 32
    print("Conversión de C a F: " + str(CaF_F))
elif ( respuesta == 2 ):
    FaC_C = ( cantidadF - 32 ) / 1.8
    print("Conversión de F a C: " + str(FaC_C))
elif ( respuesta == 3 ):
    KaC_C = cantidadK - 273.15
    print("Conversión de K a C: " + str(KaC_C))
elif ( respuesta == 4 ):
    CaK_K = cantidadC + 273.15
    print("Conversión de C a K:  " + str(CaK_K))
elif ( respuesta == 5 ):
    FaK_K = 5/9 * (cantidadF - 32) + 273.15
    print("Conversión de F a K:  " + str(FaK_K))
else:
    KaF_F = 1.8 * (cantidadK - 273.15) + 32
    print("Conversión de K a F: " + str(KaF_F))