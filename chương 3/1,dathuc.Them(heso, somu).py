class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head  # Tạo vòng
        else:
            current = self.head
            # Tìm vị trí thích hợp để chèn
            while current.next != self.head and current.next.somu > somu:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def InDaThuc(self):
        current = self.head
        if current is None:
            print("Da thuc rong")
            return
        while True:
            print(f"{current.heso}x^{current.somu}", end="")
            current = current.next
            if current != self.head:
                print(" + ", end="")
            else:
                break
        print()

# Khởi tạo một đa thức
da_thuc = DaThuc()

# Thêm các số hạng vào đa thức
da_thuc.Them(3, 2)
da_thuc.Them(5, 3)
da_thuc.Them(1, 1)

# In đa thức
da_thuc.InDaThuc()