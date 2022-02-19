nivel = float(input("Escribe el nivel de agua en la cisterna ")) 


if(nivel < 0):
    print("Hay FUGA en la cisterna")
elif(nivel == 0):
    print("Encender bomba de agua")
elif(nivel > 0 and nivel <= 2):
    print("Acelerar bomba de agua")
elif(nivel > 2 and nivel <= 4 ):
    print("¡Bomba trabajando!")
elif(nivel > 4 and nivel <= 6 ):
    print("Desacelerar bomba de agua")
elif(nivel > 6):
    print("Apagar bomba de agua")
else:
    print("¡¡¡Desbordamiento de agua en Cisterna!!!")