# Given the root of a binary tree, return the level order traversal of 
# its nodes' values. (i.e., from left to right, level by level).
# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # tree is empty
        if root is None:
            return []

        queue, tmpQueue = deque(), deque()
        queue.append(root)
        
        retList, tmpList = [[root.val]], []

        while queue:
            node = queue.popleft()

            if node.left is not None:
                tmpQueue.append(node.left)
                tmpList.append(node.left.val)

            if node.right is not None:
                tmpQueue.append(node.right)
                tmpList.append(node.right.val)
            
            if len(queue) == 0 and len(tmpQueue) > 0:
                queue = tmpQueue
                retList.append(tmpList)
                tmpQueue, tmpList = deque(), []

        return retList


