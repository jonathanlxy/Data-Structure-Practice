"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list

Example:
    Input:
        list A: 1 -> 3 -> 5 -> 6 -> NULL
        list B2 -> 4 -> 7 -> NULL
    Output:
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL
"""

def MergeLists(nodeA, nodeB):
    ## Base case
    # Both None means reached end, return None
    if not nodeA and not nodeB:
        return None
    # If one list is finished, return the other remaining list
    elif not nodeA:
        return nodeB
    elif not nodeB:
        return nodeA
    # Otherwise, compare two nodes, attached the recursive conparison result 
    # to the smaller smaller node
    if nodeA.data <= nodeB.data:
        nodeA.next = MergeLists(nodeA.next, nodeB)
        return nodeA
    else:
        nodeB.next = MergeLists(nodeA, nodeB.next)
        return nodeB