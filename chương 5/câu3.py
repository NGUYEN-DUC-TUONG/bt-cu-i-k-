class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None
    # Phương thức cay.SoNutLa() trả về số nút lá của cây
    def SoNutLa(self):
        return self._SoNutLa(self.root)
    # Phương thức đệ quy để tính số nút lá của cây
    def _SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self._SoNutLa(node.left) + self._SoNutLa(node.right)

# Ví dụ
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print("Số nút lá của cây:", tree.SoNutLa())