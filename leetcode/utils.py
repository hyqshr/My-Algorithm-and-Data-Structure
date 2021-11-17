#Linked listnode part
# Algorithm part
def findIntersect(A, B):
    len_a = 0
    len_b = 0
    pointer_a = A
    pointer_b = B

    # count head A and head B with pointer
    while pointer_a:
        len_a += 1
        pointer_a = pointer_a.next
    while pointer_b:
        len_b += 1
        pointer_b = pointer_b.next

    # find the difference and offset it
    if len_a > len_b:
        diff = len_a - len_b
        while diff:
            A = A.next
            diff -= 1
    else:
        diff = len_b - len_a
        while diff:
            B = B.next
            diff -= 1

    # find the same address
    while A and B:
        if A == B:
            return A.val
        A = A.next
        B = B.next
    return -1

# Other part

# head datastructure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# create head with number, fill in number based on list
def initListNode(nums):
    for i in range(len(nums)):
        if i == 0:
            listnode = pointer = ListNode(nums[i])
            continue
        pointer.next = ListNode(nums[i])
        pointer = pointer.next
    return listnode


# append intersect to two head A and B for testing
def appendListNode(A, B, nums):
    common = initListNode(nums)

    pointer = A
    # iterate through to the last one
    while pointer.next:
        pointer = pointer.next
    pointer.next = common

    pointer = B
    # iterate through to the last one
    while pointer.next:
        pointer = pointer.next
    pointer.next = common

    return A, B

def printListNode(listNode):
    x = []
    while listNode:
        x.append(listNode.val)
        listNode = listNode.next
    print(x)
    return x

# print question like dp
def printList(data):
    n = len(data)
    for idx,i in enumerate(data):

        if idx == 0:
            print('[',i,',')
        elif idx == n-1:
            print(' ',i,']')
            print('\n')
        else:
            print(' ',i,',')

#Tree part
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

def printLL(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)


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
    nums = [1, 2, 3, 4, 5]
    root = buildFromList(nums)
    inorder(root)