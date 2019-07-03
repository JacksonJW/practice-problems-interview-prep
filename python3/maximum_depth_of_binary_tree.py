class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.max_depth = 0
        self.root = root

    def MaxDepth(self):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.visit(self.root, 0)
        return self.max_depth

    def visit(self, current_node, count):
        if current_node is None:
            return
        count += 1
        self.max_depth = max(count, self.max_depth)
        self.visit(current_node.left, count)
        self.visit(current_node.right, count)


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
bin_tree = BinaryTree(node)
print('The max depth of the tree should be 3 and it is: ' + str(bin_tree.MaxDepth()))
