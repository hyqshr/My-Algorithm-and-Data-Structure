# class Solution:
#     def partition(self, s):
#         dp = [[] for _ in range(len(s) + 1)]
#         dp[-1] = [[]]
#         for i in range(len(s) - 1, -1, -1):
#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] == s[i:j][::-1]:
#                     for each in dp[j]:
#                         dp[i].append([s[i:j]] + each)
#         return dp[0]
# Solution().partition("aab")

def minimumTotal(triangle):
    res = 0
    for i in range(len(triangle)):
        res += min(triangle[i])
    return res
print(minimumTotal([[-1],[2,3],[1,-1,-3]]))