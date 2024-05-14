class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self):
        return self._SoNutTrungGian(self.root)

    def _SoNutTrungGian(self, node):
        # Kiểm tra nếu nút là None, tức là không có nút nào
        if node is None:
            return 0
        # Kiểm tra nếu nút không phải là lá và không phải là gốc (có ít nhất một cây con)
        elif (node.left is not None or node.right is not None) and (node.left is not None or node.right is not None):
            # Đếm nút trung gian và đệ quy đếm số nút trung gian ở cây con bên trái và bên phải
            return 1 + self._SoNutTrungGian(node.left) + self._SoNutTrungGian(node.right)
        else:
            # Nếu không phải nút trung gian, tiếp tục đệ quy xuống cây con bên trái và bên phải
            return self._SoNutTrungGian(node.left) + self._SoNutTrungGian(node.right)
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

# In số nút trung gian của cây
print("Số nút trung gian của cây:", tree.SoNutTrungGian())