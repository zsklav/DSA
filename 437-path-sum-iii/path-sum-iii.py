# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if root is None:
            return 0
        def dfs(node,currsum):
            if node is None:
                return 0
            currsum+=node.val
            count=0
            if currsum==targetSum:
                count+=1
            count+=dfs(node.left,currsum)
            count+=dfs(node.right,currsum)
            return count
        ans=dfs(root,0)
        ans+=self.pathSum(root.left,targetSum)
        ans+=self.pathSum(root.right,targetSum)
        return ans
        