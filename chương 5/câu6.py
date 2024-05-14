class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def KiemTraAVL(self):
        return self._KiemTraAVL(self.root) != -1

    def _KiemTraAVL(self, node):
        if node is None:
            return 0

        left_height = self._KiemTraAVL(node.left)
        if left_height == -1:
            return -1

        right_height = self._KiemTraAVL(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

# Ví dụ minh họa
if __name__ == "__main__":
    # Tạo cây nhị phân là cây AVL
    avl_tree = CayNhiPhan()
    avl_tree.root = Node(10)
    avl_tree.root.left = Node(5)
    avl_tree.root.right = Node(15)
    avl_tree.root.left.left = Node(3)
    avl_tree.root.left.right = Node(7)

    # Kiểm tra cây
    if avl_tree.KiemTraAVL():
        print("Cây là một cây AVL.")
    else:
        print("Cây không phải là một cây AVL.")