
#K eggs. N floors
from leetcode.utils import printList
class Solution:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
                printList(dp)
            if dp[m][K] >= N:
                return m

print(Solution().superEggDrop(2,6))