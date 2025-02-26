def count_valid_numbers(N):
    if N == 1:
        return 7  # No podemos tener ceros iniciales

    dp = [[0] * 8 for _ in range(N + 1)]

    # Caso base: Un solo dígito (sin ceros iniciales)
    for d in range(1, 8):
        dp[1][d] = 1

    # Llenamos la tabla DP
    for i in range(2, N + 1):  # Desde 2 hasta N dígitos
        for d in range(8):  # Último dígito del número
            for prev in range(8):  # Posibles valores previos
                if not (d == 0 and prev == 0) and not (d == 4 and prev == 4):
                    dp[i][d] += dp[i - 1][prev]

    # Sumamos todos los valores dp[N][d] para obtener la respuesta final
    return sum(dp[N])

# Ejemplo de uso
N = 10
print(count_valid_numbers(N))  # Imprime la cantidad de números válidos

