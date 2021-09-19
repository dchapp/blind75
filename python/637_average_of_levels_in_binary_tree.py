# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        levels = {}
        
        def bfs(node, level):
            if level not in levels:
                levels[level] = [node.val]
            else:
                levels[level].append(node.val)
            if node.left is not None:
                bfs(node.left, level+1)
            if node.right is not None:
                bfs(node.right, level+1)
        
        bfs(root, 0)
        return [ sum(vals)/len(vals) for level,vals in levels.items() ]
