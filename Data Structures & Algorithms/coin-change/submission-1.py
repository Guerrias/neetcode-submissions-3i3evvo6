class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [math.inf] * (amount + 1)
        minCoins[0] = 0

        for value in range(1, amount+1):
            for coin in coins:
                if coin > value:
                    continue
                minCoins[value] = min(minCoins[value], minCoins[value - coin] + 1)
        
        return -1 if minCoins[amount] == math.inf else minCoins[amount]