def depth_first_traversal_iterative(graph, source):
    res = []
    stack = [source]
    while stack:
        curr = stack.pop()
        res.append(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)
    return res


def depth_first_traversal_recursive(graph, source):
    res = []

    def dfs(curr):
        res.append(curr)
        if not graph[curr]:
            return
        for neighbor in graph[curr]:
            dfs(neighbor)

    dfs(source)
    return res


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    print(depth_first_traversal_recursive(graph=graph, source='a'))
