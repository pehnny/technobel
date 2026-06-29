def coin_change(coins: list[int], change: int) -> int:
    dp = [float('inf') for _ in range(change + 1)]
    dp[0] = 0
    for amount in range(1, len(dp)):
        for coin in coins:
            i = amount - coin
            if 0 <= i < len(dp):
                dp[amount] = 1 + min(dp[amount], dp[i])
    return int(dp[change]) if dp[change] != float('inf') else -1
