# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head= cur= ListNode()
        l, r= list1, list2
        
        while l and r:
            if l.val< r.val:
                cur.next= l
                l= l.next
            else:
                cur.next= r
                r= r.next
            
            cur= cur.next
        
        if l:
            cur.next= l
        else:
            cur.next= r
        
        return head.next
                