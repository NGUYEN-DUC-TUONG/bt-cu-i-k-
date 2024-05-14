class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def ChuaDinh(self, v):
        return v < self.V
# Ví dụ minh họa
dt = DoThi(5)
print("Đỉnh 3 có tồn tại trong đồ thị:", dt.ChuaDinh(3))
print("Đỉnh 7 có tồn tại trong đồ thị:", dt.ChuaDinh(7))