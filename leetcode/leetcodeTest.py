class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        greater_map = {x: -1 for x in nums1}
        stack = []

        for num in nums2:
            #只要stack有东西 并且 当前数字 大于 stack的最后一项，就pop出来
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num in greater_map:
                    greater_map[prev_num] = num
            stack.append(num)

        return [greater_map[x] for x in nums1]
nums1 = [4,1,2]
nums2 = [1,3,4,2]
if __name__ == '__main__':
    Solution().nextGreaterElement(nums1,nums2)