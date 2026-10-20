
def coin_change(coins, amount):
    if amount < 0 or any(c <= 0 for c in coins):
        raise ValueError("Invalid coin or amount")

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(
                    dp[value],
                    dp[value - coin] + 1
                )

    return dp[amount] if dp[amount] != float("inf") else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
