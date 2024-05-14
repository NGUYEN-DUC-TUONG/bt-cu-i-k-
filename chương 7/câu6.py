class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCung(self, u, v):
        self.adj[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for u in range(self.V):
            if v in self.adj[u]:
                count += 1
        return count
# Ví dụ minh họa
dt = DoThi(5)
dt.themCung(0, 1)
dt.themCung(1, 2)
dt.themCung(2, 0)
dt.themCung(2, 3)
dt.themCung(3, 4)
dt.themCung(4, 2)

print("Số cung vào đỉnh 0:", dt.SoCungVao(0))
print("Số cung vào đỉnh 1:", dt.SoCungVao(1))
print("Số cung vào đỉnh 2:", dt.SoCungVao(2))
print("Số cung vào đỉnh 3:", dt.SoCungVao(3))
print("Số cung vào đỉnh 4:", dt.SoCungVao(4))