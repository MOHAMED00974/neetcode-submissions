# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.result= True
    def MaxDepth(self, node): 
        if not node:
            return 0
        
        right, left= self.MaxDepth(node.right), self.MaxDepth(node.left)
        if abs(right- left)>1: 
            self.result= False
        return max(right, left)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.MaxDepth(root)
        return self.result