#implement RBTree without deletion

import random


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Init node with val with red color
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        # find the parent to be inserted
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        # The loop will continue until parent of new node is black
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left
                # if uncle is red,then case 1
                # 1. 把uncle由红变黑；
                # 2. 把parent(A)变黑
                # 3. 把爷爷(c)变红；
                # 4. 把指针从z移到爷爷
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent

                else:
                    #case 2: instant rorate to case 3
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    #case 3:
                    # 1.flip parent and g'parent color
                    # 2. call rotation on grandparent
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def search(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Recursive function to find inorder predecessor for a given key in a BST



    def sort(self):
        res = []
        def inorder(root, res):
            # Recursive travesal
            if root:
                inorder(root.left, res)
                print(root.val)
                res.append(root.val)
                inorder(root.right, res)
        res = inorder(self.root,res)
        return res

def findPredecessor(tree, node):
    # predecessor is the value right smaller than node.val,so try find the max in the left
    if node.left is not tree.nil:
        return findMax(tree, node.left)

    #else,it will left most parent
    parent = node.parent
    while (parent is not None) and node == parent.left:
        node = parent
        parent = parent.parent

    if parent:
        return parent.val
    else:
        return None

#utils:
def findMin(tree,node):
    '''

    :param tree:
    :param node:
    :return: Min value start from given node
    '''
    current = node

    while (current.left != tree.nil):
        current = current.left

    return current

def findMax(tree,node):
    '''

    :param tree:
    :param node:
    :return: Max value start from given node
    '''
    current = node

    while (current.right != tree.nil):
        current = current.right

    return current.val


def findSuccessor(tree,n):
    '''

    :param tree:
    :param n:
    :return sucessor of node n:
    '''
    # if node.right,find Successor in node.right
    if n.right is not tree.nil:
        return findMin(tree,n.right)

    # else,Successor is above the
    p = n.parent
    while (p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num-1))
    return nums


def main():
    #create test case
    tree = RBTree()
    insert_nus = [random.randint(0,100) for i in range(30)]
    # insert_nus = [1,5,7,8,33,22,11,55]
    print(insert_nus)
    print('insert_nus: ',sorted(insert_nus))

    for x in insert_nus:
        tree.insert(x)
    #test search func
    print('search',tree.search(7).val)

    #test sort func

    # print('sort',tree.sort())
    #test findMin and findMax func
    print('max',findMax(tree,tree.root))
    print('min',findMin(tree,tree.root).val)

    #test findSuccessor and findPredecessor

    x = tree.search(sorted(insert_nus)[0])
    print('The successor of {} is :'.format(x.val),findSuccessor(tree,x).val)
    print('The predecessor of {} is :'.format(x.val), findPredecessor(tree, x))


if __name__ == '__main__':
    main()