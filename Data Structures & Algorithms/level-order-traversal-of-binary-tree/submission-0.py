# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr_queue = [root]
        curr_next = []
        nums = []
        res = []
        while len(curr_queue) > 0:
            nums = []
            for t in curr_queue:
                nums.append(t.val)
                if t.left:
                    curr_next.append(t.left)
                if t.right:
                    curr_next.append(t.right)
            res.append(nums)
            curr_queue = curr_next.copy()
            curr_next.clear()
        return res

        