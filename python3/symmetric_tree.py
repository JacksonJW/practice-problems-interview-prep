# Given a binary tree, check whether it is a mirror
# of itself(ie, symmetric around its center).

# For example, this binary tree[1, 2, 2, 3, 4, 4, 3]
# is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#      1
#     / \
#    2   2
#     \   \
#     3    3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isSymmetric(self):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [self, self]
        while len(q) != 0:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)

print('result expected to be true and the output is: ' + str(node.isSymmetric()))
