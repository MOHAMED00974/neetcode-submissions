# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def MaxDepth(self, node)-> tuple[int, int]: 
        if not node: 
            return 0, 0

        right= self.MaxDepth(node.right)
        left= self.MaxDepth(node.left)
        LastDiff= max(right[1], left[1])

        return  max(right[0], left[0])+1, max(LastDiff, (right[0]+left[0]))    
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        return self.MaxDepth(root)[1]
        

