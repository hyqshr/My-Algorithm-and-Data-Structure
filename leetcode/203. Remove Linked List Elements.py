from leetcode.utils import initListNode,printListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = initListNode([1,2])
printListNode(head)
x = head
x = x.next
printListNode(head)
printListNode(x)