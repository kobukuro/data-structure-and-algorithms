# problem:https://structy.net/problems/depth-first-values

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# n = # of nodes
# Time:O(n), Space:O(n)
def depth_first_values_iterative(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return res


def depth_first_values_recursive(root):
    if not root:
        return []
    res = []

    def dfs(curr):
        res.append(curr.val)
        if curr.left:
            dfs(curr.left)
        if curr.right:
            dfs(curr.right)

    dfs(root)
    return res


def depth_first_values_recursive_alvin(root):
    if not root:
        return []
    left_values = depth_first_values_recursive_alvin(root.left)
    right_values = depth_first_values_recursive_alvin(root.right)
    return [root.val, *left_values, *right_values]


if __name__ == '__main__':
    # ['a', 'b', 'd', 'e', 'c', 'f']
    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
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
    print(depth_first_values_recursive_alvin(a))
