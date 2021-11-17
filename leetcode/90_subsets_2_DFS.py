class Solution(object):
    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret,0)
        return ret

    def dfs(self, nums, path, ret,c):
        print(c*'\t','call dfs( nums: ',nums,' ',',path: ',path, ')  recursive depth: ',c)
        ret.append(path)
        for i in range(len(nums)):
            print(c * '\t','current i',i)
            if i > 0 and nums[i] == nums[i - 1]:
                print(c * '\t','skip the number','nums[i]: {},nums[i - 1]: {}'.format(nums[i],nums[i - 1]))
                continue
            self.dfs(nums[i + 1:], path + [nums[i]], ret,c+1)
        print(' ')

nums = [1, 2, 2]
Solution().subsetsWithDup(nums)