num_alumnnos = int(input("Ingrese el número de alumnos de la escuela: "))  #Preguntamos el cardinal del cpnjunto
name_alumnos=[]  #Definimnos los conjuntos
prom_alumnos=[]
print("Escribe el nombre de cada alumno seguido de su promedio")
n=1
while n<=num_alumnnos:                         #Estabblecemos un bucle para recolectar la información de los N alumnos 
    name = input("Nombre del alumno: ")
    prom = int(input("Promedio de {}: ".format(name)))
     
    name_alumnos.append(name)          #Agregamos la información a los conjuntos
    prom_alumnos.append(prom)
    n+=1

def Ordenar_Inserción (a, b, c):
    for i in range(1, c):  
        promedio = a[i]   #guardamos el n elemento
        alumno= b[i]
        j=i-1
        
        while (j>=0 and a[j]>promedio):   #comparamos el n elemento con el n-1 elemento
            a[j+1] = a[j]   #si es que es mayor n-1 elemento, le asignamos la posición n
            b[j+1] = b[j]
            j=j-1

        a[j+1]=promedio    #en la posición n-1 colocamos al que salió menor en la comparación de arriba

        b[j+1]= alumno


Ordenar_Inserción(prom_alumnos, name_alumnos, num_alumnnos)
print("Los promedios ordenados son: ")
for k in range(num_alumnnos):   #imprimimos los N alumnos con sus N promedios ya ordenados
    print(name_alumnos[k], prom_alumnos[k], sep=" ---> ")