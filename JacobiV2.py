
import pandas as pd
import numpy as np

def recolectar_Datos():
    n = int(input("Introduzca el tamaño del sistema de ecuación: "))
    print(generar_encabezado(n))
    x = [[ 0 for i in range(n + 1)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            x[i][j] = int(input("Ingresa el coeficiente del temino X" + str(j + 1) + " para la fila " + str(i + 1) + ": "))
        x[i][n] = int(input("Ingresa la constante para la fila " + str(i + 1) + ": "))
    return x, n

def generar_encabezado(n):
    cadena = ""
    for j in range(n):
        for i in range(n):
            if(i == 0):
                cadena = cadena + "[]X1+"
            elif(i == n - 1):
                cadena = cadena + "[]X" + str(n) + " = []\n"
            else:
                cadena = cadena + "[]X" + str(i + 1) + "+"

    return cadena

def verificar_Diagonal_Dominante(x, n):
    check = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            if (i != j):
                sum += abs(x[i][j])
        if(x[i][i] >= sum):
            check += 1
        else:
            print("La diagonal de la matriz no es dominante.")
            return False
    if(check == n):
        #print("La diagonal de la matriz es dominante.")
        return True


def despejar_Sistema_Ecuaciones(x, n):
    y = [[ 0 for i in range(n + 1)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            y[i][j] = x[i][j] / x[i][i]
            if i != j:
                y[i][j] = (-y[i][j])
        y[i][n] = x[i][n] / x[i][i]
    return y

def  metodo_jacobi (ecuaciones, error, n):
    z = [[ 0 for i in range(n * 2)]for j in range(2)]
    ite = 0
    while (ite < 2 or condicion_error(n,z, ite, error) == False):
        if ite == 0:
            for i in range(n):
                res = 0
                for j in range(n):
                    if(i != j):
                        res += ecuaciones[i][j]*0
                res += ecuaciones[i][n]
                if(ecuaciones[i][i] > 0):
                    z[ite][i] = res
                else:
                    z[ite][i] = -res
        else:
            for i in range(n):
                res = 0
                for j in range(n):
                    if(i != j):
                        res += ecuaciones[i][j]*z[ite - 1][j]
                res += ecuaciones[i][n]
                if(ecuaciones[i][i] > 0):
                    z[ite][i] = res
                else:
                    z[ite][i] = -res
                z[ite][i + n] = calculo_de_error(z[ite][i], z[ite - 1][i])
        ite += 1
        z.append([ 0 for i in range(n * 2)])
    return z

def condicion_error(n, z, ite, error):
    res = True
    for i in range(n, n * 2, 1):
        if(z[ite - 1][i] > error):
            res = False
            break
    return res

def calculo_de_error(x_actual,x_anterior):
    if(x_actual != 0):
        error = abs((x_actual - x_anterior) / x_actual)
    else:
        error = nullcontext
    return error

def generar_encabezado_DF(n):
    cadena = []
    for i in range(n):
        cadena.append('X' + str(i + 1))
    for i in range(n):
        cadena.append('EX' + str(i + 1))

    #print(cadena)
    return cadena

def main():
    matriz, n = recolectar_Datos()

    if(verificar_Diagonal_Dominante(matriz, n) == True):
        ecuaciones = despejar_Sistema_Ecuaciones(matriz, n)
        resultado = metodo_jacobi(ecuaciones, 0.00000001, n)

    matriz = np.array(resultado)
    df = pd.DataFrame(matriz, columns=generar_encabezado_DF(n))
    df.index = np.arange(1, len(df) + 1)

    print(df)


main()