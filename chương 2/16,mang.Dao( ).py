def find_max_area(matrix, visited, row, col, current_area):
    # Hàm đệ quy để tìm kích thước vùng đảo từ ô hiện tại

    # Di chuyển đến các ô kề cạnh
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
            # Đánh dấu ô đã xem xét
            visited[new_row][new_col] = True
            # Tăng diện tích của vùng đảo
            current_area[0] += 1
            # Gọi đệ quy cho ô kề cạnh
            find_max_area(matrix, visited, new_row, new_col, current_area)

def max_island_area(matrix):
    max_area = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                current_area = [1]  # Số ô đất của vùng đảo hiện tại
                visited[i][j] = True
                find_max_area(matrix, visited, i, j, current_area)
                max_area = max(max_area, current_area[0])
    return max_area

# VD:
matrix = [
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1]
]

print("Maximum island area:", max_island_area(matrix))
