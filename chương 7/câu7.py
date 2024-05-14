class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCung(self, u, v):
        self.adj[u].append(v)

    def SoCungRa(self, v):
        return len(self.adj[v])
# Ví dụ minh họa
dt = DoThi(5)
dt.themCung(0, 1)
dt.themCung(1, 2)
dt.themCung(2, 0)
dt.themCung(2, 3)
dt.themCung(3, 4)
dt.themCung(4, 2)

print("Số cung ra từ đỉnh 0:", dt.SoCungRa(0))
print("Số cung ra từ đỉnh 1:", dt.SoCungRa(1))
print("Số cung ra từ đỉnh 2:", dt.SoCungRa(2))
print("Số cung ra từ đỉnh 3:", dt.SoCungRa(3))
print("Số cung ra từ đỉnh 4:", dt.SoCungRa(4))