# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size= 0
        cur= head

        while cur:
            size+= 1
            cur= cur.next

        trgt= size-n

        if trgt== 0:
            return head.next
        
        cur, nxt= head, head.next
        trgt-= 1

        while trgt:
            cur= cur.next
            nxt= nxt.next
            trgt-= 1
            
        cur.next= nxt.next
        return head

