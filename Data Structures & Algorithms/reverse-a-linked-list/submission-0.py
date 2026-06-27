# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next== None:
            return head

        before, current= head, head.next

        head.next= None

        while current != None:
            after= current.next
            current.next= before

            before= current
            current= after
        
        return before


            
