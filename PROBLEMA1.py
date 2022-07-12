print("Indique la cantidad de valores del conjunto A")

N = int(input())

if N > 0:
    print("La cantidad de valores es correcta")
    
    positivos=0
    negativos=0
    nulos=0
    suma_negativos=0
    producto_positivos=1

    for i in range(N):
        print("Ingrese el numero",i+1)
        numeros = int(input())

        if numeros > 0:
            positivos = positivos + 1
            producto_positivos *= numeros
                
        elif numeros<0:
            negativos = negativos + 1
            suma_negativos = suma_negativos + numeros

        else:
            nulos = nulos + 1
        
        porcentaje = (nulos/N)*100
        
        
    print("------------------------------------------------------")  
    if negativos >= 1:
        print("  La sumatoria de los valores negativos de A es: ",suma_negativos, "")
    else:
        print("     El conjunto A no tiene valores negativos")
    print("------------------------------------------------------")
    if positivos >= 1:
        print("  El producto de los valores positivos de A es: ", producto_positivos," ")
    else:
        print("     El conjunto A no tiene valores positivos")
    print("------------------------------------------------------")
    if nulos >= 1:
        print("  El porcentaje de valores nulos de A es: %.2f"%porcentaje, "%       ")
    else:
        print("     El conjunto A no tiene valores nulos")
    print("------------------------------------------------------")

else:
    print("La cantidad de valores es incorrecta")