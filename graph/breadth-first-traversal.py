from collections import deque


# breadth first traversal is only possible iteratively
def breadth_first_traversal(graph, source):
    res = []
    queue = deque()
    queue.append(source)
    while queue:
        curr = queue.popleft()
        res.append(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)
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
    print(breadth_first_traversal(graph=graph, source='a'))
