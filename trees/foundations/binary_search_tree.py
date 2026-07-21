from tree_node import TreeNode

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val > node.val:
            node.right = self._insert(node.right, val)
        elif val < node.val:
            node.left = self._insert(node.left, val)
        return node

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # found node to be deleted
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node):
        while node.right:
            node = node.right
        return node
        
    # ---------- TRAVERSALS ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    # ---------- VALIDATE ----------
    def is_valid_bst(self):
        return self._is_valid(self.root, float('-inf'), float('inf'))

    def _is_valid(self, node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (self._is_valid(node.left, low, node.val) and
                self._is_valid(node.right, node.val, high))

    # ---------- HEIGHT ----------
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1  # empty tree convention
        return 1 + max(self._height(node.left), self._height(node.right))

    # ---------- PRETTY PRINT ----------
    def print_tree(self):
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, prefix, is_left):
        if node is not None:
            self._print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
            self._print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

if __name__ == "__main__":
    # ---------- DEMO ----------
    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Tree structure:")
    bst.print_tree()
    # Expected:
    #     ┌── 80
    # ┌── 70
    # │   └── 60
    # 50
    # │   ┌── 40
    # └── 30
    #     └── 20

    print("\nInorder (should be sorted):", bst.inorder())
    # Expected: [20, 30, 40, 50, 60, 70, 80]

    print("Search 40:", bst.search(40))   # Expected: True
    print("Search 99:", bst.search(99))   # Expected: False

    print("Height:", bst.height())        # Expected: 2

    print("Is valid BST:", bst.is_valid_bst())  # Expected: True

    # --- Delete leaf node ---
    bst.delete(20)
    print("\nAfter deleting 20 (leaf):", bst.inorder())
    # Expected: [30, 40, 50, 60, 70, 80]

    # --- Delete node with one child ---
    bst.delete(30)
    print("After deleting 30 (one child):", bst.inorder())
    # Expected: [40, 50, 60, 70, 80]

    # --- Delete node with two children ---
    bst.delete(70)
    print("After deleting 70 (two children):", bst.inorder())
    # Expected: [40, 50, 60, 80]

    bst.print_tree()
    # Expected structure after all deletes:
    #     ┌── 80
    # ┌── 60
    # 50
    # └── 40