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
    
    def RutGon(self):
        current = self.Head
        prev = None
        coeffs = {}
        while current:
            if current.SoMu in coeffs:
                coeffs[current.SoMu] += current.HeSo
                prev.KeTiep = current.KeTiep
                current = prev.KeTiep
            else:
                coeffs[current.SoMu] = current.HeSo
                prev = current
                current = current.KeTiep
        self.Head = None
        for somu, heso in coeffs.items():
            self.Them(heso, somu)
    
    def Tich(self, dathuc2):
        result = DaThuc()
        current1 = self.Head
        while current1:
            current2 = dathuc2.Head
            while current2:
                result.Them(current1.HeSo * current2.HeSo, current1.SoMu + current2.SoMu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep
        result.RutGon()
        return result
    
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


print("Nhap da thuc 1:")
dathuc1 = nhap_da_thuc()

print("\nNhap da thuc 2:")
dathuc2 = nhap_da_thuc()

print("\nDa thuc 1:")
dathuc1.InDaThuc()

print("\nDa thuc 2:")
dathuc2.InDaThuc()

result = dathuc1.Tich(dathuc2)
print("\nTich cua hai da thuc:")
result.InDaThuc()