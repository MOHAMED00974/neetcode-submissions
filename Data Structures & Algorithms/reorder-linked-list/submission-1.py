# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack= []
        cur= head
        
        while cur:
            stack.append(cur)
            cur= cur.next
        
        cur= head

        while True:
            tmp= cur.next
            nxt= stack.pop()
            
            if cur== nxt:
                cur.next= None
                return
            
            cur.next= nxt
            
            if nxt== tmp:
                nxt.next= None
                return

            nxt.next= tmp
            
            cur= tmp
        

