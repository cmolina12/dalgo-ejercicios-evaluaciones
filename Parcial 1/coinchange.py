#- Dada una matriz de monedas $m[]$ de tamaño n y un valor objetivo T, donde $m[]$ representa las monedas de diferentes denominaciones. Usted tiene un suministro infinito de cada una de las monedas. la tarea consiste en encontrar el numero minimo de monedas necesarias para poder sumar $T$.

##	- $m=[1,2,5]$
#	- $T=11$
#	- *La mínima cantidad de monedas es 3, coger dos de 5 y una de 1*

monedas = [1,3,5,7,8,9,10]
T= 11

def coin_change(monedas, T):
    if T == 0:
        return 0 # Llegamos al caso base y se acaba la recursividad
    if T < 0:
        return float('inf')
    
    min_coins = float('inf') # Inicializamos el minimo de monedas a infinito
    
    for moneda in monedas:
        numero_monedas = coin_change(monedas, T-moneda) 
        if numero_monedas != float('inf'):
            min_coins = min(min_coins, 1+numero_monedas)
        
    return min_coins

print(coin_change(monedas, T)) # 3