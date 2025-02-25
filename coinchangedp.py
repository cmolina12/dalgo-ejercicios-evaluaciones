


def coin_change_debug(monedas, T, memo={}):
    if T in memo:
        return memo[T]
    
    if T == 0:
        return 0
    if T < 0:
        return float('inf')

    min_coins = float('inf')

    for moneda in monedas:
        num_coins = coin_change_debug(monedas, T - moneda, memo)
        print(f"El numero de monedas para {T - moneda} es {num_coins}")  # 🔹 Imprime cada paso
        if num_coins != float('inf'):
            min_coins = min(min_coins, 1 + num_coins)

    memo[T] = min_coins
    print(f"dp({T}) = {memo[T]}")  # 🔹 Imprime cada paso
    return memo[T]

monedas = [1, 3, 4]
T = 6
resultado = coin_change_debug(monedas, T)
print(f"Resultado final: {resultado}")
