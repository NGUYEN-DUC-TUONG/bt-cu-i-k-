class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def themCanh(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited, parent):
        visited[v] = True
        for u in self.adj[v]:
            if not visited[u]:
                if self.DFS(u, visited, v):
                    return True
            elif parent != u:
                return True
        return False

    def ChuTrinh(self):
        visited = [False] * self.V

        for v in range(self.V):
            if not visited[v]:
                if self.DFS(v, visited, -1):
                    return True
        return False
# Ví dụ minh họa có chu trình
dt = DoThi(6)
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 0)
dt.themCanh(2, 3)
dt.themCanh(3, 4)
dt.themCanh(4, 5)
dt.themCanh(5, 3)

print("Đồ thị có chu trình:", dt.ChuTrinh())
# Ví dụ minh họa không có chu trình
dt2 = DoThi(4)
dt2.themCanh(0, 1)
dt2.themCanh(1, 2)
dt2.themCanh(2, 3)
print("Đồ thị không có chu trình:", dt2.ChuTrinh())