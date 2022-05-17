# recursion without memoization
# time:O(2^n+m), space:O(n+m)
# def grid_traveler(m, n):
#     if m == 0 or n == 0:
#         return 0
#     if m == 1 and n == 1:
#         return 1
#     return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

# recursion with memoization
# reduce to only distinct nodes
# time:O(n*m), space:O(n+m)
# def grid_traveler(m, n, memo=None):
#     if memo is None:
#         memo = {}
#     key = f'{m},{n}'
#     if key in memo:
#         return memo[key]
#     if m == 0 or n == 0:
#         return 0
#     if m == 1 or n == 1:
#         return 1
#     memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
#     return memo[key]

# time:O(n*m), space:O(n*m)
# tabulation
def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    table = []
    for r in range(m + 1):
        row = []
        for c in range(n + 1):
            row.append(0)
        table.append(row)
    table[1][1] = 1
    # print(table)
    for row in range(len(table)):
        for col in range(len(table[0])):
            # print(row, col)
            if row + 1 < len(table):
                table[row + 1][col] += table[row][col]
            if col + 1 < len(table[0]):
                table[row][col + 1] += table[row][col]
    return table[-1][-1]


if __name__ == '__main__':
    print(grid_traveler(m=2, n=3))  # 3
    # print(grid_traveler(m=18, n=18))  # 2333606220
