import sys
Matriz_x = []
Matriz_y = []

def datos():
    
    #Matriz 1 datos

    rows_matrix1 = int(input("Insert number of  el rows  "))
    columns_matrix1 = int(input("Insert number of Columns "))

    matriz1_longitud = rows_matrix1  * columns_matrix1

    for recorrido in range(0,matriz1_longitud):
        recolector= int(input("Insert numbers: "))
        Matriz_x.append(recolector)


    #Matriz 2 datos 
    rows_matrix2 = int(input("Insert number of rows  (Matrix 2)  ")) 
    columns_matrix2 = int(input("Insert number of Columns (Matrix 2)  "))

    matriz2_longitud = rows_matrix2 * columns_matrix2 

    for recorrido in range(0,matriz2_longitud):
        recolector= int(input("Insert numbers: "))
        Matriz_y.append(recolector)
     
    return Matriz_x,Matriz_y

#Eleccion 

print("CHOOSE ONE OPTION, YOU CAN SELECT ONLY ONE")
print("1. SUM ") 
print("2. SUBTRACTION") 
print("3. MULTIPLICATION")   
print("4. GAUSS JORDAN")   

elecction = int(input("Insert your option "))

#Suma 
if elecction == 1:
    datos()
    for mike in range(len(Matriz_x)):
        print(Matriz_x[mike] + Matriz_y[mike])

#Resta 
elif elecction == 2:
    datos()
    for mike in range(len(Matriz_x)):
        print(Matriz_x[mike] - Matriz_y[mike])

#Multiplicacion 
elif elecction == 3:
    matrizA = []
    MatrizB = []
    matriz_final=[]

    filasA = int(input("Ingresa numero de filas "))
    ColumnaA =int(input("Ingresa numero de Columnas "))
    filasB = int(input("Ingresa numero de filas "))
    ColumnaB =int(input("Ingresa numero de Columnas "))

    if (ColumnaA != filasB):
       print("Operacion no valida")
       sys.exit()

    else:

        print("-----Matriz A -----")
        for q in range(filasA):
            matrizA.append([0]*ColumnaA)
        for w in range(filasA):
            for  e in range(ColumnaA):
                matrizA[w][e] = int(input("Elemento %d,%d:  "%(w,e)))
        
        print("-----Matriz B -----")
        for q in range(filasB):
            MatrizB.append([0]*ColumnaB)
        for w in range(filasB):
            for  e in range(ColumnaB):
                MatrizB[w][e] = int(input("Elemento %d,%d:  "%(w,e)))

        for x in range(filasA):
            matriz_final.append([0]*ColumnaB)
            for y in range(ColumnaB):
                matriz_final[x][y] = 0
           
        for i in range(filasA):
            for j in range(ColumnaA):
                for k in range(ColumnaB):
                    matriz_final[i][k] = matriz_final[i][k] + (matrizA[i][j] * MatrizB[j][k])

        print(matriz_final)


#Gauss Jordan 
elif elecction == 4:
    
    print("Hola")

    