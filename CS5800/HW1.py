

# Algorithm part
def findIntersect(A, B):
    len_a = 0
    len_b = 0

    #set pointers to find the length
    pointer_a = A
    pointer_b = B

    # count head A and head B with pointer
    while pointer_a:
        len_a += 1
        pointer_a = pointer_a.next
    while pointer_b:
        len_b += 1
        pointer_b = pointer_b.next

    # find the length difference and offset it by moving the longer head
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


# create head with numbers in list , fill in number based on list
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


# Test case
if __name__ == '__main__':
    a = [5, 4, 3]
    b = [4, 8, 3, 1, 2]
    common = [9, 8, 7]
    A = initListNode(a)
    B = initListNode(b)
    A, B = appendListNode(A, B, common)

    print(findIntersect(A, B))
