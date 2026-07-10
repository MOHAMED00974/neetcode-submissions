# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head= ListNode()
        cur= head

        still= 0
        nds= []

        for lst in lists:
            nds.append(lst)
            if lst:
                still += 1
        
        while still> 0:
            tmp= 0
            for lst in range(len(nds)):
                if nds[tmp]== None or (nds[lst] and nds[lst].val< nds[tmp].val):
                    tmp= lst
            cur.next= nds[tmp]
            cur= cur.next

            nds[tmp]= nds[tmp].next
            if nds[tmp]== None:
                still -= 1

        return head.next


