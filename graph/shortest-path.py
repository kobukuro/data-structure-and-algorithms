# problem:https://structy.net/problems/shortest-path
# linear complexity
from collections import deque


def shortest_path(edges, src, dst):
    graph = {}
    for edge in edges:
        node_a, node_b = edge
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    # print(graph)
    queue = deque()
    # 防止cycle
    visited = set()
    # 要記得把和src的距離也要加進去
    queue.append((src, 0))
    while queue:
        node, distance = queue.popleft()
        if node == dst:
            return distance
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                queue.append((nei, distance + 1))
    return -1


if __name__ == '__main__':
    # 2
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    src = 'w'
    dst = 'z'
    print(shortest_path(edges=edges, src='w', dst='z'))
