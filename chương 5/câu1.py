class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None
    # Phương thức cay.SoNut() trả về số nút của cây
    def SoNut(self):
        return self._SoNut(self.root)
    # Phương thức đệ quy để tính số nút của cây
    def _SoNut(self, node):
        if node is None:
            return 0
        else:
            return self._SoNut(node.left) + self._SoNut(node.right) + 1

# Ví dụ 
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# In số nút của cây
print("Số nút của cây:", tree.SoNut())