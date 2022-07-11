print("Indique la cantidad de valores del conjunto A")

N = int(input())

if N > 0:
    positivos=0
    negativos=0
    nulos=0
    suma_negativos=0
    producto_positivos=1

    for i in range(N):
        print("Ingrese el numero",i+1)
        numeros = int(input())
        
        if numeros > 0:

            producto_positivos = producto_positivos * numeros
            
        elif numeros < 0:           

            suma_negativos = suma_negativos + numeros

        else:
            nulos = nulos + 1
        
        porcentaje = (nulos/N)*100
        
    print("------------------------------------------------------")  
    print("  La sumatoria de los valores negativos de A es: ",suma_negativos, "")
    print("------------------------------------------------------")
    print("  El producto de los valores positivos de A es: ", producto_positivos," ")
    print("------------------------------------------------------")
    print("  El porcentaje de valores nulos de A es: %.2f"%porcentaje, "%       ")
    print("------------------------------------------------------")

else:
    print("La cantidad de valores es incorrecta")