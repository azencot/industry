
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def zigzagLevelOrder(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    # edge case
    if root is None:
        return []

    queue, queue2, level = deque([root]), deque(), 0
    values, level_vals = [], []
    while queue:
        node = queue.popleft()
        level_vals.append(node.val)

        if node.left is not None:
            queue2.append(node.left)
        if node.right is not None:
            queue2.append(node.right)

        if len(queue) == 0:
            # print from left to right
            if level % 2 == 0:
                values.append(level_vals)
            # print from right to left
            else:
                values.append(level_vals[::-1])
            queue = queue2
            queue2 = deque()
            level_vals, level = [], level+1

    return values


# [3,9,20,null,null,15,7]

TreeNode7 = TreeNode(7)
TreeNode15 = TreeNode(15)
TreeNode20 = TreeNode(20, TreeNode15, TreeNode7)
TreeNode9 = TreeNode(9)
root = TreeNode(3, TreeNode9, TreeNode20)
print(zigzagLevelOrder(None, root))
