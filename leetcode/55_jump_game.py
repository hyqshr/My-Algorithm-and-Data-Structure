#在每个位置，都计算每一个 position 能到达的最大数max(m,i+n)
#动态规划，更新当前最大步骤
#开始的时候先检查上一次的规划是否大于现在的位置
class Solution:
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    nums = [0,1]
    Solution().canJump(nums)