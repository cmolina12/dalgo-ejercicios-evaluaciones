
# Dada una matriz de monedas $m[]$ de tamaño n y un valor objetivo T, donde $m[]$ representa las monedas de diferentes denominaciones. Usted tiene un suministro infinito de cada una de las monedas. la tarea consiste en encontrar el numero minimo de monedas necesarias para poder sumar $T$.

# Ejemplo:

# Input: m[] = {1, 2, 3}, T = 4
# Output: 2
# Explicacion: Se puede obtener 4 sumando 2 y 2

# Resolver con programacion dinamica

def coin_change_memo(monedas, T, memo={}):
    if T in memo:  # 🔹 Si ya calculamos dp(T), lo devolvemos en O(1)
        return memo[T]

    if T == 0:
        return 0
    if T < 0:
        return float('inf')

    min_coins = float('inf')

    for moneda in monedas:  
        num_coins = coin_change_memo(monedas, T - moneda, memo)
        if num_coins != float('inf'):
            min_coins = min(min_coins, 1 + num_coins)

    memo[T] = min_coins  # 🔹 Guardamos el resultado
    return min_coins

m = [1, 2, 3]
T = 95

print(coin_change_memo(m, T))  # Output: 2