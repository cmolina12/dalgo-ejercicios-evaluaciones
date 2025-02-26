def max_coins(cofres):
    if not cofres:
        return 0
    N = len(cofres)
    if N == 1:
        return cofres[0]
    if N == 2:
        return max(cofres[0], cofres[1])

    # Inicializar DP
    dp = [0] * N
    dp[0] = cofres[0]
    dp[1] = max(cofres[0], cofres[1])

    for i in range(2, N):
        dp[i] = max(dp[i-1], cofres[i] + dp[i-2])

    return dp[-1]  # 🔹 Retornamos la máxima cantidad de monedas posible

cofres = [5, 19, 12, 20, 22, 16, 17, 23, 21]
max_monedas = max_coins(cofres)

print(f"Máximo de monedas: {max_monedas}")  # Output: 79
