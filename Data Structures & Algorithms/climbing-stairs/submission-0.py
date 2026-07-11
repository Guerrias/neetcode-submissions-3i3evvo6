class Solution:
    def climbStairs(self, n: int) -> int:
        numberOfWay = [0] * (n + 1)
        numberOfWay[0] = 1
        numberOfWay[1] = 1

        for step in range(2, n+1):
            numberOfWay[step] = numberOfWay[step - 1] + numberOfWay[step - 2]
        return numberOfWay[n]