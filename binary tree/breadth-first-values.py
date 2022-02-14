# problem:https://structy.net/problems/breadth-first-values
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# n = # of nodes
# Time:O(n), Space:O(n)
def breadth_first_values(root):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        curr = queue.popleft()
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res


if __name__ == '__main__':
    # ['a', 'b', 'c', 'd', 'e', 'f']
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(breadth_first_values(a))
