class TreeNode(object):
    def __init__(self, x, p = None, q = None):
        self.val = x
        self.left = p
        self.right = q


def recoverPath(p, parents):
    node, path_p = p, []
    while node is not None:
        path_p.append(node)
        node = parents[node.val]
    return path_p

def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    
    # DFS the tree to find path to p and q
    queue, parents = [root], {root.val: None}
    found_p, found_q = False, False
    while queue:
        node = queue.pop()

        if node.left is not None:
            queue.append(node.left)
            parents[node.left.val] = node

            if node.left == p:
                found_p = True
            if node.left == q:
                found_q = True
        
        if node.right is not None:
            queue.append(node.right)
            parents[node.right.val] = node

            if node.right == p:
                found_p = True
            if node.right == q:
                found_q = True

        if found_p and found_q:
            break

    # recover paths
    path_p = recoverPath(p, parents)[::-1]
    path_q = recoverPath(q, parents)[::-1]

    # find last occurance in paths that matches
    n = min(len(path_p), len(path_q))
    for j in range(n-1,-1,-1):
        if path_p[j].val == path_q[j].val:
            return path_p[j]


node7 = TreeNode(7)
node4 = TreeNode(4)
node2 = TreeNode(2, node7, node4)
node6 = TreeNode(6)
node1 = TreeNode(1)
node5 = TreeNode(5, node6, node2)
root = TreeNode(3, node5, node1)
print(lowestCommonAncestor(None, root, node5, node4).val)