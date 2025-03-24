
def minimum_rope_cutting(n, cuts):
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)

    dp = [[0] * m for _ in range(m)]

    for length in range(2, m):
        for i in range(m-length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (cuts[j] - cuts[i]))

    return dp[0][m-1]

if __name__=="__main__":
    n = 7
    cuts = [1, 3, 4, 5]
    print(f'Minimum cost: {minimum_rope_cutting(n, cuts)}')
