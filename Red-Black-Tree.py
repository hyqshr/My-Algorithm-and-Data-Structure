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
        self.nil = RBNode(float('-inf'))
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

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
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
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
    def findPredecessor(root, prec, key):

        # base case
        if root is None:
            return prec

        # if a node with the desired value is found, the predecessor is the maximum value
        # node in its left subtree (if any)
        if root.data == key:
            if root.left:
                return findMax(root.left)

        # if the given key is less than the root node, recur for the left subtree
        elif key < root.data:
            return findPredecessor(root.left, prec, key)

        # if the given key is more than the root node, recur for the right subtree
        else:
            # update predecessor to the current node before recursing
            # in the right subtree
            prec = root
            return findPredecessor(root.right, prec, key)

        return prec

    def sort(self):
        res = []
        def inorder(root, res):
            # Recursive travesal
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
        res = inorder(self.root,res)
        return res

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

    return current.val

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

def findPredecessor(tree,p):
    '''
    recursive implement of findPredecessor

    :param node:
    :return: its Predecessor
    '''
    predecessor = None
    root = tree.root
    while root is not tree.nil:
        if p.val > root.val:
            predecessor = root
            root = root.right
        else:
            root = root.left
    if predecessor:
        print('predecessor of {} found!: {}'.format(p.val,predecessor.val))
    else:
        print('No Predecessor!')
    return predecessor





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
    print('Successor of {} found!: {}'.format(n.val,p.val))
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
    insert_nums = [1,2,3,5,11,15]
    print('insert nums: ',insert_nums)
    for x in insert_nums:
        tree.insert(x)
    #test search func
    print('search',tree.search(5).val)
    print('search',tree.search(7).val)

    #test sort func
    # tree.sort()
    # print(tree)

    #test findMin and findMax func
    print('max',findMax(tree,tree.root))
    print('min',findMin(tree,tree.root))
    #
    print('\ntest findSuccessor and findPredecessor\n')
    x = tree.search(3)
    findSuccessor(tree,x)
    findPredecessor(tree, x)
    print()

    x = tree.search(11)
    findSuccessor(tree,x)
    findPredecessor(tree, x)


if __name__ == '__main__':
    # nums = ''
    # for _ in range(0,30):
    #     nums += str(random.randint(1,100))
    #     nums += ' '
    #
    #
    # with open('./input_nums.txt','w') as f:
    #     f.write(nums)
    # with open('./input_nums.txt','r') as f:
    #     nums = f.readlines()[0]
    # nums = nums.split()

    main()