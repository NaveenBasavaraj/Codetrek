# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.max_height(root.left)
        right_height = self.max_height(root.right)

        diameter = left_height + right_height

        sub = max(self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
    
    def max_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.max_height(root.left), 
        self.max_height(root.right))
        
