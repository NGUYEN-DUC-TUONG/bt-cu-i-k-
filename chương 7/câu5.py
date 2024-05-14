class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def BacDinh(self, v):
        return len(self.adj[v])
# Ví dụ minh họa
dt = DoThi(5)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 3)
dt.themCanh(2, 4)

print("Bậc của đỉnh 0:", dt.BacDinh(0))
print("Bậc của đỉnh 1:", dt.BacDinh(1))
print("Bậc của đỉnh 2:", dt.BacDinh(2))
print("Bậc của đỉnh 3:", dt.BacDinh(3))
print("Bậc của đỉnh 4:", dt.BacDinh(4))