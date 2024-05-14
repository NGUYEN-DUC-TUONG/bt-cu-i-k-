class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None
    # Phương thức cay.ChieuCao() trả về chiều cao của cây
    def ChieuCao(self):
        return self._ChieuCao(self.root)
    # Phương thức đệ quy để tính chiều cao của cây
    def _ChieuCao(self, node):
        if node is None:
            return 0
        else:
            left_height = self._ChieuCao(node.left)
            right_height = self._ChieuCao(node.right)
            return max(left_height, right_height) + 1

# Ví dụ 
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# In chiều cao của cây
print("Chiều cao của cây:", tree.ChieuCao())
