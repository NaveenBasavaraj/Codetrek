from foundations.tree_node import TreeNode


class DFS:
    def preorder(self, root, result=None):
        if not result:
            result = []
        if not root:
            return result
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)
        return result

    def preorder_iterative(self, root):
        result = []
        if not root:
            return result

        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.right)
        return result[::-1]

    def inorder(self, root, result=None):
        if not result:
            result = []
        if not root:
            return result
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
        return result

    def postorder(self, root, result=None):
        if not result:
            result = []
        if not root:
            return result
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)
        return result

    def preorder_simple(self, root):
        if not root:
            return []
        return (
            [root.val]
            + self.preorder_simple(root.left)
            + self.preorder_simple(root.right)
        )

    def inorder_simple(self, root):
        if not root:
            return []
        return (
            self.preorder_simple(root.left)
            + [root.val]
            + self.preorder_simple(root.right)
        )

    def postorder_simple(self, root):
        if not root:
            return []
        return (
            self.preorder_simple(root.left)
            + self.preorder_simple(root.right)
            + [root.val]
        )
