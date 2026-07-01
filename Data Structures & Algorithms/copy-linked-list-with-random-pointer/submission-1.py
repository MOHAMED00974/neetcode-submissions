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
        newHead, newHead.next= Node(0), Node(0)

        cur, newCur= head, newHead

        while cur:
            newCur= newCur.next
            newCur.val= cur.val
            cur= cur.next
            newCur.next= Node(0)
            
        newCur.next= None

        cur= head
        newCur= newHead.next

        while cur:
            itter, newIter= head, newHead.next
            while itter != cur.random:
                itter= itter.next
                newIter= newIter.next
            newCur.random= newIter
            cur= cur.next
            newCur= newCur.next
        
        return newHead.next





