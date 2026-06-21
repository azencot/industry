# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def valid_bst(self, root):

        if root is None:
            return True, float('inf'), float('-inf')

        lret, l_min_val, l_max_val = self.valid_bst(root.left)
        rret, r_min_val, r_max_val = self.valid_bst(root.right)

        lret = lret and l_max_val < root.val
        rret = rret and r_min_val > root.val
            
        return lret and rret, min(l_min_val, r_min_val, root.val), max(l_max_val, r_max_val, root.val)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """    
        return self.valid_bst(root)[0]