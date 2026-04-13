# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]
        while queue:
            new_queue = []
            first = True
            for n in queue:
                if n:
                    if first:
                        res.append(n.val)
                        first = False
                    new_queue.append(n.right)
                    new_queue.append(n.left)
            queue = new_queue
        return res

        