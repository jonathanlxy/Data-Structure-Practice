# Binary Search Tree
def sep(func):
    def f(*args, **kwargs):
        func(*args, **kwargs)
        print '\n'
    return f

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        left, right = None, None
        if self.left:
            left = self.left.data
        if self.right:
            right = self.right.data
        return 'data: {!r}\nLeft: {}\nright: {}'.format(self.data, left, right)

class BST:
    def __init__(self):
        self.root = None

    def __insert_node__(self, node, data):
        print 'Insert at {}'.format(node.data)
        if node.data > data:
            print '< Go'
            if node.left:
                self.__insert_node__(node.left, data)
            else:
                # Base case
                print '< Insert '
                node.left = Node(data)
        elif node.data < data:
            print 'Go >'
            if node.right:
                self.__insert_node__(node.right, data)
            else:
                # Base case
                print 'Insert >'
                node.right = Node(data)
        else:
            print '{!r} already exists.'.format(data)
    @sep
    def insert(self, data):
        print 'Inserting: {}'.format(data)
        if self.root:
            print 'Insert child'
            self.__insert_node__(self.root, data)
        else:
            print 'Insert root'
            self.root = Node(data)

    def __preorder__(self, node):
        print node.data
        if node.left:
            self.__preorder__(node.left)
        if node.right:
            self.__preorder__(node.right)

    def __inorder__(self, node):
        if node.left:
            self.__inorder__(node.left)
        print node.data
        if node.right:
            self.__inorder__(node.right)

    def __postorder__(self, node):
        if node.left:
            self.__postorder__(node.left)
        if node.right:
            self.__postorder__(node.right)
        print node.data

    def traverse(self, order = 0):
        '''
        Order:
        0 = Pre-order
        1 = In-order
        2 = Post-order
        '''
        if order:
            if order == 1:
                print 'In-order'
                return self.__inorder__(self.root)
            elif order == 2:
                print 'Post-order'
                return self.__postorder__(self.root)
            else:
                print 'Invalid order'
        else:
            print 'Pre-order'
            return self.__preorder__(self.root)

if __name__ == '__main__':
    tree = BST()
    nums = [32, 10, 55, 1, 19, 16, 23, 55, 79]
    for i in nums:
        tree.insert(i)

    # Pre-order
    # 32-10-1-19-16-23-55-79
    tree.traverse(0)
    # In-order
    # 1-10-16-19-23-32-55-79
    tree.traverse(1)
    # Post-order
    # 1-16-23-19-10-79-55-32
    tree.traverse(2)