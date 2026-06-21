# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_seen = float('-inf')


        def mps(root):

            if root is None:
                return float('-inf')

            lmps = mps(root.left)
            rmps = mps(root.right)

            self.max_seen = max(self.max_seen, lmps, rmps)

            # root is avoided if it makes both left/right contribution negative
            # in this case: avoid root, update max seen and return 0
            if lmps + root.val < 0 and rmps + root.val < 0:
                return max(lmps, rmps, lmps + root.val, rmps + root.val, root.val)

            # right branch
            elif lmps + root.val < 0 and rmps + root.val > 0:
                return rmps + root.val

            # left branch
            elif lmps + root.val > 0 and rmps + root.val < 0:
                return lmps + root.val

            else:
                return lmps + root.val + rmps


        curr_max = mps(root)

        return max(self.max_seen, curr_max)
