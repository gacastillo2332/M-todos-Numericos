from modulefinder import IMPORT_NAME

import pandas as pd
import numpy as np

def recolectar_Datos():
    print("Consdierando que se desea calcular el metodo Jacobi en una matriz 3x3")
    print("[]X1+[]X2+[]X3 = []\n[]X1+[]X2+[]X3 = []\n[]X1+[]X2+[]X3 = []\n")
    x = [[ 0 for i in range(4)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            x[i][j] = int(input("Ingresa el coeficiente del temino X" + str(j + 1) + " para la fila " + str(i + 1) + ": "))
        x[i][3] = int(input("Ingresa la constante para la fila " + str(i + 1) + ": "))
    return x

def verificar_Diagonal_Dominante(x):
    check = 0
    for i in range(3):
        sum = 0
        for j in range(3):
            if (i != j):
                sum += abs(x[i][j])
        if(x[i][i] >= sum):
            check += 1
        else:
            print("La diagonal de la matriz no es dominante.")
            return False
    if(check == 3):
        #print("La diagonal de la matriz es dominante.")
        return True


def despejar_Sistema_Ecuaciones(x):
    y = [[ 0 for i in range(4)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            y[i][j] = x[i][j] / x[i][i]
            if i != j:
                y[i][j] = (-y[i][j])
        y[i][3] = x[i][3] / x[i][i]
    return y

def  metodo_jacobi (ecuaciones, error):
    z = [[ 0 for i in range(6)]for j in range(2)]
    ite = 0
    while (ite < 2 or z[ite - 1][3] > error or z[ite - 1][4] > error or z[ite - 1][5] > error):
        if ite == 0:
            for i in range(3):
                res = 0
                for j in range(3):
                    if(i != j):
                        res += ecuaciones[i][j]*0
                res += ecuaciones[i][3]
                if(ecuaciones[i][i] > 0):
                    z[ite][i] = res
                else:
                    z[ite][i] = -res
        else:
            for i in range(3):
                res = 0
                for j in range(3):
                    if(i != j):
                        res += ecuaciones[i][j]*z[ite - 1][j]
                res += ecuaciones[i][3]
                if(ecuaciones[i][i] > 0):
                    z[ite][i] = res
                else:
                    z[ite][i] = -res
                z[ite][i + 3] = calculo_de_error(z[ite][i], z[ite - 1][i])
        ite += 1
        z.append([ 0 for i in range(6)])
    return z

def calculo_de_error(x_actual,x_anterior):
    error = abs((x_actual - x_anterior) / x_actual)
    return error

def main():
    matriz = recolectar_Datos()

    if(verificar_Diagonal_Dominante(matriz) == True):
        ecuaciones = despejar_Sistema_Ecuaciones(matriz)
        resultado = metodo_jacobi(ecuaciones, 0.001)

    matriz = np.array(resultado)
    df = pd.DataFrame(matriz, columns=['X1', 'X2', 'X3','EX1','EX2','EX3'])
    df.index = np.arange(1, len(df) + 1)

    print(df)


main()