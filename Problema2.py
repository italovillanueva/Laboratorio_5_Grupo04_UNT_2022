X1 = []
X2 = []
media_aritmetica = []
media_geometrica = []

valor = 0
print("Ingrese el número de pares de numeros: ")
tamaño = input()
tamaño = int(tamaño)
while tamaño<=0:
    print("Ese numero no es aceptado, intente nuevamente: ")
    tamaño = input()
    tamaño = int(tamaño)

i=0
while i < tamaño:
    print("Ingrese el número ", 1, " del par de valores número ", i+1, " (debe ser un real positivo):")
    valor = input()
    valor = float(valor)
    while valor <= 0: 
        print("El valor ingresado no es un real positivo. Pruebe de nuevo: ")
        valor = input()
        valor = float(valor)
    X1.append(valor)
    print("Ingrese el número ", 2, " del par de valores número ", i+1, " (debe ser un real positivo):")
    valor = input()
    valor = float(valor)
    while valor<=0: 
        print("El valor ingresado no es un real positivo. Pruebe de nuevo: ")
        valor = input()
        valor = float(valor)
    X2.append(valor)
    i+=1

i=0
j=0 #contabiliza el número de veces en que la media aritmetica es menor que la media geometrica
while i<tamaño:
    media_aritmetica.append((X1[i]+X2[i])/2)
    print("La media aritmetica de los números ", X1[i], " y ", X2[i], " es: ", media_aritmetica[i])
    media_geometrica.append((X1[i]*X2[i])**0.5)
    print("La media geométrica de los números ", X1[i], " y ", X2[i], " es: ", media_geometrica[i])
    if media_aritmetica[i] < media_geometrica[i]: j = j+1
    i+=1

i=tamaño-1
k=-1 #lista en la que la media aritmetica es igual a la media geometrica por primera vez
while i>=0:
    if media_aritmetica[i] == media_geometrica[i]: 
        k=i
    i-=1

print("La media aritmetica ha sido menor que la media geométrica el ", abs(100*j/i), "%", " de las veces.")

if k == -1:
    print("En ningún par se cumple que la media aritmetica sea igual a la media geometrica.")
else: print("El primer par de valores en la lista donde la media aritmetica es igual a su media geométrica es", X1[k], "y", X2[k], "(el par de valores número", k+1,").")