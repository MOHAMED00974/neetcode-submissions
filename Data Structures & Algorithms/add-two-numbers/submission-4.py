# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def carry(cur):
            if cur.val< 10:
                return
            cur.val-= 10
            
            if cur.next:
                cur.next.val+= 1
                carry(cur.next)
                return
            cur.next= ListNode(1)

        l, r= l1, l2

        while l and r:
            l.val+= r.val
            carry(l)
            prev= l
            l= l.next
            r= r.next

        
        if l:
            return l1
        else:
            prev.next= r
            return l1