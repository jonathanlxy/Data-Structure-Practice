# Singly linked list implementation
'''
Requirements:
    class LinkedList = Node1 -> Node2, ...
        Singly linked list wrapper
        Properties:
            root: the root node
            size: return the size of the list
        Methods:
            push(node): insert a node at the beginning
            drop(value): find the first node with given value and drop it
            insert(new_value, target_value): 
                insert a node with new_value after the node with target_value
            has_cycle(): detect if the list contains a cycle
    class Node = data, pointer
        Node of the singly linked list. Each contains value and pointer to
        the next node
        Methods:
            update(value): update the node with new value
'''
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, value):
        # Insert at beginning
        newnode = Node(value)
        if self.size:
            newnode.next = self.root
        self.root = newnode
        self.size += 1

    def append(self, value):
        # Attach to the end
        newnode = Node(value)
        if self.size:
            node = self.root
            while node.next:
                node = node.next
            node.next = newnode
        else:
            self.root = newnode
        self.size += 1

    def return_list(self):
        if not self.root:
            return []
        whole_list = [self.root.value]
        node = self.root
        for i in xrange(1, self.size):
            whole_list.append(node.next.value)
            node = node.next
        return whole_list

    def drop(self, look_up_value):
        # When list is empty
        if not self.size:
            print 'Empty list'
            return None
        # When root = target
        elif self.root.value == look_up_value:
            self.root = self.root.next
            self.size -= 1
            return None
        node0 = self.root
        node1 = node0.next
        # Loop through the list & drop target
        for i in xrange(1, self.size):
            if node1.value == look_up_value:
                node0.next = node1.next
                self.size -= 1
                return None
            node0, node1 = node1, node1.next
        print 'Target not found.'

    def insert(self, target_value, new_value):
        newnode = Node(new_value)
        node = l.root
        while node:
            if node.value != target_value:
                node = node.next
            else:
                node.next, newnode.next = newnode, node.next
                self.size += 1
                return None
        print 'Target not found'

    def has_cycle(self):
        '''
        Any no cycle case will eventually reach out of bound or NoneType.next 
        not exist error. Using except to handle all those errors will be 
        significantly faster than using differnt validation conditions
        '''
        try:
            node1, node2 = self.root, self.root.next
            while node1 != node2:
                node1, node2 = node1.next, node2.next.next
            return True
        except:
            return False

if __name__ == '__main__':
    print 'Contruction test - initiate'
    l = LinkedList()
    print 'List: {}, size: {}'.format(l.return_list(), l.size)
    
    print 'push test - push 0 to 9'
    [l.push(i) for i in xrange(10)]
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Append test - append 10 to 19'
    [l.append(i) for i in xrange(10, 20)]
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Drop test'
    print 'Drop 9'; l.drop(9)
    print 'List: {}, size: {}'.format(l.return_list(), l.size)
    print 'Drop 19'; l.drop(19)
    print 'List: {}, size: {}'.format(l.return_list(), l.size)
    print 'Drop 10'; l.drop(10) 
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Insert test'
    print 'Insert 991 after 12'
    l.insert(12, 991)
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Insert 992 after first value'
    l.insert(l.root.value, 992)
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Insert 993 after last value'
    l.insert(18, 993)
    print 'List: {}, size: {}'.format(l.return_list(), l.size)

    print 'Cycle detection'
    print 'Current l.has_cycle(): {}'.format(l.has_cycle())
    print 'Insert a bad node with value = 666 & next = second element of list'
    badnode = Node(666)
    badnode.next = l.root.next
    node = l.root
    while node.next:
        node = node.next
    node.next = badnode
    print 'Current l.has_cycle(): {}'.format(l.has_cycle())