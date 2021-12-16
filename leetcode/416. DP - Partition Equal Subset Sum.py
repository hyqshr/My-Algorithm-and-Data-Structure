class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        #如果是奇数，直接返回
        if total_sum & 1:
            return False
        half_sum = total_sum // 2
        #dp[0][0]是base case设置为True
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]


print(Solution().canPartition([1,5,11,3]))