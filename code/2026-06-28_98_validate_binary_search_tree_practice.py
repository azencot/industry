"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: True

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: False
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 10**4].
    -2**31 <= Node.val <= 2**31 - 1
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node, low, high):

            # stopping condition
            if node is None:
                return True

            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert sol.isValidBST(root1) is True

    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(root2) is False

    root3 = TreeNode(2, TreeNode(2), TreeNode(2))
    assert sol.isValidBST(root3) is False

    root4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert sol.isValidBST(root4) is False

    root5 = TreeNode(-2147483648, None, TreeNode(2147483647))
    assert sol.isValidBST(root5) is True

    print("all tests passed")
