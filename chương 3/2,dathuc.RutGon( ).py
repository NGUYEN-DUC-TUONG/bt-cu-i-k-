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

    def RutGon(self):
        current = self.head
        while current.next != self.head:
            next_node = current.next
            while next_node != self.head:
                if current.somu == next_node.somu:
                    current.heso += next_node.heso
                    current.next = next_node.next
                next_node = next_node.next
            current = current.next

        # Loại bỏ các số hạng có hệ số bằng 0
        prev = None
        current = self.head
        while current.next != self.head:
            if current.heso == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            prev = current
            current = current.next
        # Kiểm tra số hạng cuối cùng
        if current.heso == 0:
            if prev:
                prev.next = current.next
            else:
                self.head = None

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

# Tạo một đa thức
da_thuc = DaThuc()

# Nhập số hạng cho đa thức
while True:
    heso = int(input("Nhap he so: "))
    somu = int(input("Nhap so mu: "))
    da_thuc.Them(heso, somu)
    tiep_tuc = input("Nhap them so hang? (Y/N): ")
    if tiep_tuc.lower() != 'y':
        break

# In đa thức trước khi rút gọn
print("Da thuc truoc khi rut gon:")
da_thuc.InDaThuc()

# Rút gọn đa thức
da_thuc.RutGon()

# In đa thức sau khi rút gọn
print("Da thuc sau khi rut gon:")
da_thuc.InDaThuc()