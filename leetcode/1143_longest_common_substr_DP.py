class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)

        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[j - 1] == text2[i - 1] else max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]