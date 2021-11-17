class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
def insert(root,node):
	if root is None:
		root=node
	else:
		if root.val<node.val:
			if root.right is None:
				root.right=node
			else:
				insert(root.right,node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left,node)

def buildFromList(nums):
    if len(nums) < 2:
        return Node(nums[0])
    else:
        root = Node(nums[0])
        for i in nums[1:]:
            num = Node(i)
            insert(root,num)
    return root
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def depth(p):
            if not p:
                return 0
            print(p.val)
            left, right = depth(p.left), depth(p.right)

            print(left,right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans
if __name__ == '__main__':
    # a = [5, 4, 3]
    # b = [4, 8, 3, 1, 2]
    # intersect = [9, 8, 7]
    #
    # A = initListNode(a)
    # B = initListNode(b)
    # A, B = appendListNode(A, B, intersect)
    #
    # print(findIntersect(A, B))
    # a = [[1,2,3],[4,5,6],[7,8,9]]
    # printList(a)

    # Tree
    nums = [2, 1, 4, 3, 5]
    root = buildFromList(nums)
    print(Solution().diameterOfBinaryTree(root))