class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [math.inf] * (amount+1)
        result[0] = 0

        for value in range(amount+1):
            for coin in coins:
                if coin > value:
                    continue
                result[value] = min(result[value], result[value - coin] + 1)
        
        return -1 if result[amount] == math.inf else result[amount]