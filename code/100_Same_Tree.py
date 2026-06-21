# Given the roots of two binary trees p and q, write a function to check 
# if they are the same or not.

# Two binary trees are considered the same if they are structurally 
# identical, and the nodes have the same value.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # idea: traverse layer-by-layer (binary tree), use deque
        # if every node along the way equals in p and q, continue, otherwise stop

        # another way would be to traverse separately; prepare two lists per tree
        # one list for values, one binary list for nodes; if the list equal, the tree are equal

        # the second option is less efficient in the average case of non same trees (since it always traverse the whole tree)
        if p == None and q != None or p != None and q == None:
            return False
        elif p == None and q == None:
            return True 

        pairs = deque()
        pairs.append((p, q))

        while pairs:

            pn, qn = pairs.popleft()
            
            if pn.val != qn.val:
                return False

            lpn, rpn = pn.left != None, pn.right != None
            lqn, rqn = qn.left != None, qn.right != None

            if lpn != lqn or rpn != rqn:
                return False

            if lpn:
                pairs.append((pn.left, qn.left))

            if rpn:
                pairs.append((pn.right, qn.right))

        return True
