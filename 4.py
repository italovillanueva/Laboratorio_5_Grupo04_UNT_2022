'''La secuencia de Tribonacci Tn se define de la siguiente manera: 
Dado n encontrar el valor de Tn'''

n_termino = int(input("Ingrese la posición n del enésimo término: "))

def tribonacci(n):  #definimos la función recursiva
    if n>2:
        enesimo = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)   #definición de la sucesión 
    elif n==2:
        enesimo=1             #definimos los primeros valores especiales de la sucesión"
    elif n==1:
        enesimo=1
    elif n==0:
        enesimo=0
    else:
        print("recuerda que n debe ser mayor o igual a 0")

    return enesimo   #la función devuelve el enésimo término

print(tribonacci(n_termino))