# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        bunny, turtle= head, head

        while turtle and turtle.next:
            bunny= bunny.next
            turtle= turtle.next.next
            if bunny== turtle:
                return True

        return False