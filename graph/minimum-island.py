# problem:https://structy.net/problems/minimum-island
# r = # rows, c = # cols
# Time: O(rc), Space: O(rc)
def minimum_island(grid):
    rows, cols = len(grid), len(grid[0])
    res = None
    visited = set()  # 使用set 防止cycle(infinite loop)

    def dfs(r, c):
        if r < 0 or r == rows or c < 0 or c == cols:
            return 0
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        if grid[r][c] == 'W':
            return 0
        size = 1
        size += dfs(r + 1, c)
        size += dfs(r - 1, c)
        size += dfs(r, c + 1)
        size += dfs(r, c - 1)
        return size

    for row in range(rows):
        for col in range(cols):
            size = dfs(row, col)
            if size > 0:
                if not res:
                    res = size
                else:
                    if size < res:
                        res = size
    return res


if __name__ == '__main__':
    # 2
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(minimum_island(grid=grid))
