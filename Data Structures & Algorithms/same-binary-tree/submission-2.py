# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.same= True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not self.same: 
            return False
        
        if p is None or q is None: 
            if p is None and q is None: 
                return True
            self.same= False
            return False
        
        if p.val!= q.val: 
            self.same= False
            return False
        
        if not (self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)): 
            return False
        
        return self.same
        
        

