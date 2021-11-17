class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1: return 0

        diff = [prices[i + 1] - prices[i] for i in range(n - 1)]
        dp, dp_max = [0] * (n + 1), [0] * (n + 1)
        for i in range(n - 1):
            dp[i] = diff[i] + max(dp_max[i - 3], dp[i - 1])
            dp_max[i] = max(dp_max[i - 1], dp[i])
            print(dp)
            print(dp_max)
            print('\n')

        return dp_max[-3]
if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    #diff [1,1,-3,2]
    print(Solution().maxProfit(prices))
