

# Solucion normal

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Explicacion: La funcion fibonacci se llama a si misma recursivamente. Sumamos los dos numeros anteriores para obtener el siguiente numero de la serie. Lento, aplicamos programacion dinamica.

def fibonacci_dp(n,memo={}):
    if n in memo: return memo[n]
    
    if n == 0: return 0
    if n == 1: return 1 
    
    memo[n] = fibonacci_dp(n-1,memo)+fibonacci_dp(n-2,memo)

    return fibonacci_dp(n-1)+fibonacci_dp(n-2)


print(fibonacci_dp(10)) # 55
print(fibonacci_dp(50)) # 12586269025

