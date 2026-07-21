from collections import deque
from tree_node import TreeNode

def build_tree_from_list(values: list) -> TreeNode:
    if not values or values[0] is None:
        # because root Node cannot be None
        return None
    # start with root
    root = TreeNode(values[0]) 
    queue = deque([root])
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.popleft()
        
        if i < n:
            # assign values to left child
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        
        if i < n:
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)                    

if __name__ == "__main__":
    root = build_tree_from_list([1, 2, 3, 4, 5])
    print_tree(root)
    