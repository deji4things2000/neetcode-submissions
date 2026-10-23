"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hm = {}

        #Create a copy of every node
        cur = head
        while cur:
            hm[cur] = Node(cur.val)
            cur = cur.next
        
        #Then connect the next and random pointers
        cur = head
        while cur:
            copy = hm[cur]
            copy.next = hm.get(cur.next)
            copy.random = hm.get(cur.random)

            cur = cur.next
        
        return hm[head]

