# problem:https://structy.net/problems/undirected-path
# n = # nodes, e = # edges
# time:O(e), space:O(n)
def undirected_path(edges, src, dst):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    # print(graph)
    # 使用set,新增item以及check item有沒有在set裡都只要O(1)
    visited = set()

    def dfs(curr):
        if curr == dst:
            return True
        if curr in visited:
            return False
        visited.add(curr)
        for nei in graph[curr]:
            if dfs(nei):
                return True
        return False

    return dfs(src)


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    src = 'j'
    dst = 'm'
    print(undirected_path(edges=edges, src=src, dst=dst))
