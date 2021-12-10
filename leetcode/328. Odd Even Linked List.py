class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        d1=odd=ListNode(0)
        d2=even=ListNode(0)
        i=1
        while head:
            if i%2:
                odd.next,odd=head,head
            else:
                even.next,even=head,head
            head = head.next
            i+=1
        odd.next,even.next=d2.next,None
        return d1.next

h2 = ListNode(3)
h1 = ListNode(2)
h1.next = h2
head = ListNode(1)
head.next = h1

from leetcode.utils import initListNode
head1 = initListNode([1,2,3,4,5])
head2 = initListNode([2,1,3,5,6,4,7])

head = Solution().oddEvenList(head1)
while head:
    print(head.val)
    head = head.next
