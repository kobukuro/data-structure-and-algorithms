from collections import deque


# problem:https://structy.net/problems/has-path
# 可以用DFS也可以用BFS
# 計算複雜度方法1:
# n = # nodes, e = # edges
# time:O(e), space:O(n)
# 時間複雜度為O(e),因為worse case必須尋訪每一個edge
# 空間複雜度為O(n),因為worst case會有每一個node都進到stack或是queue裡
# 計算複雜度方法2:
# n = # nodes, n^2 = # edges
# 因為當所有node都有edges連接,n^2為edges的數量
# time:O(n^2), space:O(n)
# dfs solution
# def has_path(graph, src, dst):
#     visited = set()
#
#     def dfs(curr):
#         if curr == dst:
#             return True
#         if not graph[curr]:
#             return False
#         for nei in graph[curr]:
#             if (curr, nei) not in visited:
#                 visited.add((curr, nei))
#                 if dfs(nei):  # 假如nei到dst有path，就代表src到dst有path
#                     return True
#         return False
#
#     return dfs(src)

def has_path(graph, src, dst):
    queue = deque()
    queue.append(src)
    while queue:
        curr = queue.popleft()
        if curr == dst:
            return True
        for nei in graph[curr]:
            queue.append(nei)
    return False


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    # src = 'f'
    # dst = 'k'
    src = 'j'
    dst = 'f'

    print(has_path(graph=graph, src=src, dst=dst))
