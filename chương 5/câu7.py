class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Chep(self, node):
        if node is None:
            return None
        new_node = Node(node.info)
        new_node.left = self.Chep(node.left)
        new_node.right = self.Chep(node.right)
        return new_node

    def InOrder(self, node):
        if node is not None:
            self.InOrder(node.left)
            print(node.info, end=" ")
            self.InOrder(node.right)
# Sử dụng
# Tạo cây nhị phân ban đầu
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

# Sao chép cây nhị phân
tree2 = BinaryTree()
tree2.root = tree2.Chep(tree1.root)

# In ra cây gốc ban đầu và cây sao chép để kiểm tra
print("Cây gốc:")
tree1.InOrder(tree1.root)
print("\nCây sao chép:")
tree2.InOrder(tree2.root)