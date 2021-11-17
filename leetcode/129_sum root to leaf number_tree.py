# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        self.ans = 0
        self.add(root, '')
        return self.ans

    def add(self, root, cur):
        if root:
            cur = cur + str(root.val)
            self.add(root.left, cur)
            self.add(root.right, cur)
            if not root.left and not root.right:
                self.ans += int(cur)


if __name__ == '__main__':
    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(3)

    Solution().sumNumbers(x)