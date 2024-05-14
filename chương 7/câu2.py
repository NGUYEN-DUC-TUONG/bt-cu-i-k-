class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for u in self.adj[v]:
            if not visited[u]:
                self.DFS(u, visited)

    def SoThanhPhan(self):
        visited = [False] * self.V
        count = 0

        for v in range(self.V):
            if not visited[v]:
                count += 1
                self.DFS(v, visited)

        return count
# Ví dụ minh họa
dt = DoThi(7)
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 3)
dt.themCanh(2, 4)
dt.themCanh(5, 6)
print("Số thành phần liên thông của đồ thị:", dt.SoThanhPhan())