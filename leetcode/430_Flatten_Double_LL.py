from leetcode import utils

class Solution:
    def flatten(self, head):
        if not head: return head
        stack, order = [head], []

        while stack:
            last = stack.pop()
            order.append(last)
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)

        for i in range(len(order) - 1):
            order[i + 1].prev = order[i]
            order[i].next = order[i + 1]
            order[i].child = None
            utils.printLL()
        return order[0]

Solution