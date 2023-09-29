# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        return self.testChild(root, None, targetSum, 0)
    
    def testChild(self, node, sibling, targetSum, current):
        if node == None:
            return sibling == None and targetSum == current
        current += node.val
        return self.testChild(node.left, node.right, targetSum, current) or self.testChild(node.right, node.left, targetSum, current)
