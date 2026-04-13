# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        queue = [root]
        while len(queue) > 0:
            t = queue.pop(0)
            if not t:
                res+= "null,"
            else:
                res+= str(t.val) + ","
                queue.append(t.left)
                queue.append(t.right)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        data.pop()
        print(data)
        res = None
        queue = [res]
        while len(data) > 0:
            print(f'queue is {queue}')
            
            if not res:
                curr = data.pop(0)
                if curr == "null":
                    return None
                queue.pop(0)
                res = TreeNode(int(curr),None,None)
                l = data.pop(0)
                if l != "null":
                    res.left = TreeNode(int(l),None,None)
                    queue.append(res.left)
                r = data.pop(0)
                if r != "null":
                    res.right = TreeNode(int(r),None,None)
                    queue.append(res.right)
            else:
                t = queue.pop(0)
                l = data.pop(0)
                if l != "null":
                    t.left = TreeNode(int(l),None,None)
                    queue.append(t.left)
                r = data.pop(0)
                if r != "null":
                    t.right = TreeNode(int(r),None,None)
                    queue.append(t.right)
        return res
                
        
        