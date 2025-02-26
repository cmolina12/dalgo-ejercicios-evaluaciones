def min_operations(s1, s2):
    m, n = len(s1), len(s2)

    # Inicializar la tabla dp con dimensiones (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Casos base, los de la primer afila y primera columan
    
    for j in range(n+1):
        dp[0][j] = j
    for i in range(m+1): 
        dp[i][0] = i
        
    # Llenar la tabla dp
    for i in range(1,m+1):
        for j in range(1,n+1):
            # Si son iguales
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(1+dp[i-1][j],1+dp[i][j-1])
                
    return dp[m][n] # La respuesta esta al final


# Ejemplo de uso
s1 = "blcd"
s2 = "abcd"
print(min_operations(s1, s2))  # Output esperado: 2
                