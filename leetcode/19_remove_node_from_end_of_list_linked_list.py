class Solution:
    def removeNthFromEnd(self, head, n: int):
        #建立双指针
        fast, slow = head, head
        #trick,先让fast前进n词
        for _ in range(n):
            fast = fast.next

        #如果n = length(倒数n次，也就是想remove第一个元素的时候，直接return: head.next)
        if not fast:
            return head.next

        #根据之前的trick,while结束时候，fast是最后一个元素，而slow指向倒数第n个元素
        while fast.next:
            fast, slow = fast.next, slow.next
            
        #跳过第n个元素
        slow.next = slow.next.next
        return head