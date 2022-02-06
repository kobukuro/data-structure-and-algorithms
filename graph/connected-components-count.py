# problem:https://structy.net/problems/connected-components-count
# n = # nodes, e = # edges
# time:O(e), space:O(n)
# TODO deserves to be reviewed again
def connected_components_count(graph):
    res = 0
    visited = set()

    def dfs(curr):
        if curr in visited:
            return False
        visited.add(curr)
        for nei in graph[curr]:
            dfs(nei)
        # 當curr的所有neighbors(包括neighbors的neighbors)都traverse完後,才會return true,
        # 所以代表當這裡return true時,就代表traverse完了整個connected component
        return True

    for node in graph.keys():
        # print(visited)
        if dfs(node):
            res += 1
    return res


if __name__ == '__main__':
    # 2
    graph = {0: [8, 1, 5],
             1: [0],
             5: [0, 8],
             8: [0, 5],
             2: [3, 4],
             3: [2, 4],
             4: [3, 2]}
    # 1
    # graph = {
    #     1: [2],
    #     2: [1, 8],
    #     6: [7],
    #     9: [8],
    #     7: [6, 8],
    #     8: [9, 7, 2]
    # }
    print(connected_components_count(graph=graph))
