class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None
    
    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.Head is None:
            self.Head = new_node
        else:
            current = self.Head
            while current.KeTiep:
                current = current.KeTiep
            current.KeTiep = new_node
    
    def Cong(self, dathuc):
        result = DaThuc()
        current1 = self.Head
        current2 = dathuc.Head

        while current1 and current2:
            if current1.SoMu > current2.SoMu:
                result.Them(current1.HeSo, current1.SoMu)
                current1 = current1.KeTiep
            elif current1.SoMu < current2.SoMu:
                result.Them(current2.HeSo, current2.SoMu)
                current2 = current2.KeTiep
            else:
                result.Them(current1.HeSo + current2.HeSo, current1.SoMu)
                current1 = current1.KeTiep
                current2 = current2.KeTiep

        while current1:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.KeTiep

        while current2:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.KeTiep

        result.RutGon()
        return result

    def RutGon(self):
        current = self.Head
        while current:
            prev = current
            next_node = current.KeTiep
            while next_node:
                if current.SoMu == next_node.SoMu:
                    current.HeSo += next_node.HeSo
                    prev.KeTiep = next_node.KeTiep
                prev = next_node
                next_node = next_node.KeTiep
            current = current.KeTiep

    def InDaThuc(self):
        current = self.Head
        if current is None:
            print("Da thuc rong.")
            return
        while current:
            print(f"{current.HeSo}x^{current.SoMu}", end="")
            current = current.KeTiep
            if current:
                print(" + ", end="")
        print()

# Hàm nhập đa thức
def nhap_da_thuc():
    dathuc = DaThuc()
    while True:
        heso = float(input("Nhap he so: "))
        somu = int(input("Nhap so mu: "))
        dathuc.Them(heso, somu)
        tieptuc = input("Nhap them so hang? (Y/N): ").upper()
        if tieptuc != "Y":
            break
    return dathuc

# Ví dụ sử dụng
print("Nhap da thuc 1:")
dathuc1 = nhap_da_thuc()
print("Nhap da thuc 2:")
dathuc2 = nhap_da_thuc()

print("Da thuc 1:")
dathuc1.InDaThuc()
print("Da thuc 2:")
dathuc2.InDaThuc()

ket_qua = dathuc1.Cong(dathuc2)
print("Da thuc ket qua sau khi cong:")
ket_qua.InDaThuc()