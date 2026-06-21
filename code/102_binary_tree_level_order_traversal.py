# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """

    if root is None:
            return []

    out = [[root.val]]
    queue, queue2, vals = deque([root]), deque(), []
    while queue:
        node = queue.popleft()
        
        if node.left is not None:
            queue2.append(node.left)
            vals.append(node.left.val)
        if node.right is not None:
            queue2.append(node.right)
            vals.append(node.right.val)

        if len(queue) == 0:
            queue = queue2
            if len(vals) > 0:
                out.append(vals)
            queue2, vals = deque(), []

    return out

node9 = TreeNode(9)
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
root = TreeNode(3, node9, node20)

print(levelOrder(root))

