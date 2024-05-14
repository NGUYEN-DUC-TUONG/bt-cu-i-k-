class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoSanh(self, cay2):
        return self._SoSanh(self.root, cay2.root)

    def _SoSanh(self, node1, node2):
        # Nếu cả hai nút đều là None, tức là không có gì để so sánh, trả về True
        if node1 is None and node2 is None:
            return True
        # Nếu một trong hai nút là None và nút còn lại không phải là None, trả về False
        if node1 is None or node2 is None:
            return False
        # So sánh giá trị của hai nút và gọi đệ quy để so sánh các cây con bên trái và bên phải của hai nút
        return (node1.info == node2.info and
                self._SoSanh(node1.left, node2.left) and
                self._SoSanh(node1.right, node2.right))
# Ví dụ minh họa
if __name__ == "__main__":
    # Tạo cây nhị phân thứ nhất
    cay1 = CayNhiPhan()
    cay1.root = Node(10)
    cay1.root.left = Node(5)
    cay1.root.right = Node(15)
    cay1.root.left.left = Node(3)
    cay1.root.left.right = Node(7)
    # Tạo cây nhị phân thứ hai giống cây nhị phân thứ nhất
    cay2 = CayNhiPhan()
    cay2.root = Node(10)
    cay2.root.left = Node(5)
    cay2.root.right = Node(15)
    cay2.root.left.left = Node(3)
    cay2.root.left.right = Node(7)
    # So sánh hai cây
    if cay1.SoSanh(cay2):
        print("Hai cây nhị phân giống nhau hoàn toàn.")
    else:
        print("Hai cây nhị phân không giống nhau hoàn toàn.")