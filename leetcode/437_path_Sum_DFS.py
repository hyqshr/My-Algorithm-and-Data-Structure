class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# A function to insert a new node with the given key value
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
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0: 1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
            # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        print(currPathSum,oldPathSum)
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    root = buildFromList(nums)
    print(Solution().pathSum(root,5))