"""
 Find the node at which both lists merge and return the data of that node.
 It is guaranteed that the two head Nodes will be different, and neither will be NULL.

 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

Example 1:
     1
      \
       2--->3--->NULL
      /
     1
    Return 2

Example 2:
    1--->2
          \
           3--->Null
          /
         1
    Return 3
"""

def FindMergeNode(headA, headB):
    '''
    O(N) solution
    Make two pointers start at the beginning of each list
    Each pointer loop through its own list, then jump to the beginning of 
    the other list.
    They will meet after 
    len(longer list) + len(shorter list before converge point) steps
    Maximium cost = len(listA) + len(listB) when two lists are converged 
    at the end
    
    By the time the pointer on the shorter list reaches the end, 
    distance(pointerA, pointerB) = diff(len(listA), len(listB))
    Thus when two pointers starts on the other list, the pointer from 
    the shorter list will be diff(len(listA), len(listB)) steps ahead,
    which guarantees the two pointers to meet at the convergence point
    '''
    p1, p2 = headA, headB
    
    while p1 or p2:
        # When either pointer reaches end first, send it to the head of the other list
        if not p1:
            p1 = headB
            p2 = p2.next
        elif not p2:
            p1 = p1.next
            p2 = headA
        # If both pointers still travelling, compare data & make move
        else:
            if p1.data != p2.data:
                p1, p2 = p1.next, p2.next
            else:
                return p1.data