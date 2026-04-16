"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        vis = {}
        def bfs(node):
            if node.val in vis:
                return vis[node.val]
            else:
                clone = Node()
                clone.val = node.val
                vis[clone.val] = clone
                clone.neighbors = [bfs(n) for n in node.neighbors]
                return clone
        return bfs(node)

            
        