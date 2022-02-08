# problem:https://structy.net/problems/largest-component
# n = # nodes, e = # edges
# time:O(e), space:O(n)
# TODO deserves to be reviewed again
def largest_component(graph):
    visited = set()

    def dfs(curr):
        if curr in visited:
            return 0
        visited.add(curr)
        size = 1  # current node
        for nei in graph[curr]:
            size += dfs(nei)
        return size

    res = 0
    for node in graph.keys():
        size = dfs(node)
        if size > res:
            res = size

    return res


if __name__ == '__main__':
    # 4
    # graph = {
    #     '0': ['8', '1', '5'],
    #     '1': ['0'],
    #     '5': ['0', '8'],
    #     '8': ['0', '5'],
    #     '2': ['3', '4'],
    #     '3': ['2', '4'],
    #     '4': ['3', '2']
    # }
    # 6
    # graph = {
    #     1: [2],
    #     2: [1, 8],
    #     6: [7],
    #     9: [8],
    #     7: [6, 8],
    #     8: [9, 7, 2]
    # }
    # 3
    graph = {
        0: [4, 7],
        1: [],
        2: [],
        3: [6],
        4: [0],
        6: [3],
        7: [0],
        8: []
    }
    print(largest_component(graph=graph))
