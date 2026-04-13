# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root,-101)

    def helper(self, root, maximum):
        if not root:
            return 0
        else:
            if root.val >= maximum:
                return self.helper( root.left, root.val) + 1 + self.helper( root.right, root.val) 
            else:
                return self.helper( root.left, maximum) + self.helper( root.right, maximum)
        