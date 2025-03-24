def open_coffee_shops(d, p, k):
    n = len(d)
    dp = [0] * n

    def find_prev_idx(idx):
        left, right = 0, idx-1
        while left <= right:
            mid = (left + right)//2
            if d[idx] - d[mid] >= k:
                left = mid+1
            else:
                right = mid-1
        return right

    dp[0] = p[0]
    for i in range(1, n):
        prev_idx = find_prev_idx(i)
        if prev_idx != -1:
            dp[i] = max(dp[i-1], dp[prev_idx] + p[i])
        else:
            dp[i] = max(dp[i-1], p[i])

    return dp[-1]

if __name__=="__main__":
    d = [1, 2, 5, 6, 9]
    p = [16, 20, 15, 17, 12]
    k = 4
    # d = [1, 3, 6, 10, 15]
    # p = [5, 6, 5, 8, 9]
    # k = 4
    print(open_coffee_shops(d, p, k))
