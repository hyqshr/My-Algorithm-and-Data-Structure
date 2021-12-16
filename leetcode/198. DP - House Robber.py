
class Solution:
    def rob(self, A):
        if len(A) == 1:
            return A[0]
        dp = [*A]
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]
Solution().rob([2,7,9,3,1])