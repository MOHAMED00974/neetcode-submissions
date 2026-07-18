# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(l, r):
            end= l
            past= l
            present= past.next
            future= present.next
            
            l.next= None
            while True:
                present.next= past
                if future== r:
                    return present, end
                past= present
                present= future
                future= future.next

        if k == 1:
            return head

        dummy= ListNode()
        cur= dummy

        l, r= head, head
         
        while r != None:
            cnt= 0
            while cnt< k:
                if r == None:
                    cur.next= l
                    return dummy.next
                cnt+= 1
                r= r.next
            start, end= reverse(l, r)
            cur.next= start
            cur= end
            l= r

        return dummy.next