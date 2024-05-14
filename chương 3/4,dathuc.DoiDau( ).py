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
    
    def DoiDau(self):
        current = self.Head
        while current:
            current.HeSo = -current.HeSo
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
    heso = somu = None
    while True:
        heso_input = input("Nhap he so (Nhap 'q' de ket thuc): ")
        if heso_input.lower() == 'q':
            break
        somu_input = input("Nhap so mu: ")
        try:
            heso = float(heso_input)
            somu = int(somu_input)
        except ValueError:
            print("He so phai la mot so, va so mu phai la mot so nguyen.")
            continue
        dathuc.Them(heso, somu)
    return dathuc


print("Nhap da thuc:")
dathuc = nhap_da_thuc()

print("\nDa thuc truoc khi doi dau:")
dathuc.InDaThuc()

dathuc.DoiDau()

print("\nDa thuc sau khi doi dau:")
dathuc.InDaThuc()