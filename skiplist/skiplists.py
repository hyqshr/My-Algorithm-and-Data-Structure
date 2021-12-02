#Yiqiu Huang
import random
import math


class Node:
    def __init__(self, val):
        # ```Next``` refers to the next element of the **same level**, that is, go to the right;
        # ```down``` refers to the same element of the **next level**, which is to go down;
        self.val = val
        self.next = None
        self.down = None


class Skiplist:


    def __init__(self):
        # The linked list of each level is stored in ```self.level```
        # Init value of each level linked list is negative infinity: ```-math.inf```
        # Let each higher-level linked list object point to a more basic level;

        self.levels = []
        self.max_level = 4
        prev = None
        for i in range(self.max_level):
            node = Node(-math.inf)
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node

    def _iter(self, val):
        '''
        :param val:
        :return: Max_level * nodes that right just smaller than input val
        '''

        # Enter a ``val``, as long as the next element is smaller than val, go to the right (next);
        # Otherwise, go down
        res = []
        l = self.levels[0]
        while l:
            while l.next and l.next.val < val:
                l = l.next
            res.append(l)
            l = l.down
        return res

    def search(self, target: int) -> bool:
        '''
        :param target:
        :return True if the target exist
        '''
        last = self._iter(target)[-1]
        return last.next and last.next.val == target

    def add(self, num: int) -> None:
        '''
        Add element to skiplist.
        Use probability 0.5 to decide if this value could go up to higher level.

        :param num:
        :return:
        '''
        res = self._iter(num)
        prev = None
        for i in range(len(res) - 1, -1, -1):
            node = Node(num)
            node.next, node.down = res[i].next, prev
            res[i].next = node
            prev = node
            rand = random.random()
            if rand > 0.5:
                break

    def delete(self, num: int) -> bool:
        '''
        Inplace deletion the whole level of target
        :param num:
        :return: If
        '''
        found = False
        res = self._iter(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.val == num:
                res[i].next = res[i].next.next
                found = True
        return found

if __name__ == '__main__':
    skiplist = Skiplist()
    print(len(skiplist.levels))
    print(skiplist.levels[0].down == skiplist.levels[1])
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    skiplist.search(3)
    skiplist.add(4)
    skiplist.delete(4)