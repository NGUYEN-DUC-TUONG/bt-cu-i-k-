class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def KiemTraBST(self):
        return self._KiemTraBST(self.root, float("-inf"), float("inf"))

    def _KiemTraBST(self, node, min_val, max_val):
        if node is None:
            return True       
        # Kiểm tra giá trị của nút có nằm trong khoảng cho phép không
        if node.info <= min_val or node.info >= max_val:
            return False
        # Kiểm tra nút con bên trái và bên phải với giới hạn giá trị thích hợp
        return (self._KiemTraBST(node.left, min_val, node.info) and
                self._KiemTraBST(node.right, node.info, max_val))
# Ví dụ minh họa
if __name__ == "__main__":
    # Tạo cây nhị phân không phải là BST
    tree = CayNhiPhan()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(8)
    tree.root.right.right = Node(20)

    # Kiểm tra cây
    if tree.KiemTraBST():
        print("Cây là một cây BST.")
    else:
        print("Cây không phải là một cây BST.")