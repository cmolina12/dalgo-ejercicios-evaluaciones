
# Problema Programacion Dinamica - Suma Maxima en una Matriz

# Dada una matriz a de tamaño m x n de numeros enteros (puede contener negativos), calcular la fila i y la columna j en la cual la suma de los elementos de la submatriz que va desde la fila 0 y columna 0 hasta la fila i y la columna j sea máxima

def suma_maxima_matriz(a):
    m = len(a)
    n = len(a[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = a[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + a[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + a[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + a[i][j]

    return dp[m-1][n-1], i, j


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(suma_maxima_matriz(a)) # 29