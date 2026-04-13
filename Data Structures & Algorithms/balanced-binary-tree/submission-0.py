# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def helper(root):
            if root.left is None and root.right is None:
                return (1, True)
            
            left, lbalanced = helper(root.left) if root.left else (0, True)
            right, rbalanced = helper(root.right) if root.right else (0, True)

            if not lbalanced or not rbalanced:
                return (0,False)
            return (1 + max(left,right), abs(left-right) <= 1)
        _, balanced = helper(root)
        return balanced

        


