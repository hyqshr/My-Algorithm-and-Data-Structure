from itertools import accumulate
class Solution:
    def jump(self, nums):
        t = list(accumulate([i + num for i, num in enumerate(nums)], max))
        ind, q = 0, 0
        while ind < len(nums) - 1:
            ind = t[ind]
            q += 1
        return q
if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    Solution().jump(nums)