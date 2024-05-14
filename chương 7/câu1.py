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

    def LienThong(self):
        visited = [False] * self.V

        # Chọn một đỉnh bất kỳ làm đỉnh bắt đầu cho DFS
        self.DFS(0, visited)

        # Kiểm tra xem tất cả các đỉnh có được duyệt hết không
        for i in range(1, self.V):
            if not visited[i]:
                return False
        return True
# Ví dụ minh họa
dt = DoThi(5)
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 4)

print("Đồ thị có liên thông hay không:", dt.LienThong())
