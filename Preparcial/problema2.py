
def nodos(N):
    
    dp = [0]*(N+1)

    
    # Unico arbol con un solo nodo
    dp[0] = 1
    dp[1] = 1
    
    for n in range(2,N+1):
        for i in range(n):
            dp[n] += dp[i] * dp[n-i-1]
            
            
    return dp[N]


N = 4
print(nodos(N))