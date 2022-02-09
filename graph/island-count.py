# problem:https://structy.net/problems/island-count
# TODO deserves to be reviewed again
# r = # rows, c = # cols
# Time: O(rc), Space: O(rc)
def island_count_alvin(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    res = 0

    def dfs(r, c):
        if r < 0 or r == rows or c < 0 or c == cols:
            return False
        if (r, c) in visited:
            return False
        if grid[r][c] == 'W':
            return False
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return True

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col):
                res += 1
    return res


def island_count_mine(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r == rows or c == cols or r < 0 or c < 0:
            return
        if (r, c) in visited:
            return
        visited.add((r, c))
        if grid[r][c] == 'W':
            return
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for ri, ci in directions:
            dfs(r + ri, c + ci)

    res = 0
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and (r, c) not in visited:
                dfs(r, c)
                res += 1
            else:
                visited.add((r, c))
    return res


if __name__ == '__main__':
    # 3
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(island_count_alvin(grid=grid))
