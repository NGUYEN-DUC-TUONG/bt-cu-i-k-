class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def CayCon(self, node1, node2):
        # Nếu cây 2 rỗng, luôn là cây con của cây 1
        if node2 is None:
            return True
        # Nếu cây 1 rỗng, không thể là cây con của cây 2
        if node1 is None:
            return False
        # Nếu nút gốc của cả hai cây giống nhau
        # Kiểm tra xem cây con bên trái và bên phải của cây 1 có chứa cây 2 không
        return (node1.info == node2.info) and self.CayCon(node1.left, node2.left) and self.CayCon(node1.right, node2.right)
# Tạo cây 1
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
# Tạo cây 2
tree2 = BinaryTree()
tree2.root = Node(2)
tree2.root.left = Node(4)
tree2.root.right = Node(5)

# Kiểm tra xem cây 2 có phải là cây con của cây 1 không
if tree1.CayCon(tree1.root, tree2.root):
    print("Cay 2 la cay con cua cay 1")
else:
    print("Cay 2 khong la cay con cua cay 1")
