class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited, target):
        visited[v] = True
        if v == target:
            return True
        for u in self.adj[v]:
            if not visited[u]:
                if self.DFS(u, visited, target):
                    return True
        return False

    def DuongDi(self, v1, v2):
        visited = [False] * self.V
        return self.DFS(v1, visited, v2)
# Ví dụ minh họa
dt = DoThi(5)
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 4)

print("Có đường đi từ đỉnh 0 đến đỉnh 4:", dt.DuongDi(0, 4))
print("Có đường đi từ đỉnh 3 đến đỉnh 0:", dt.DuongDi(3, 0))