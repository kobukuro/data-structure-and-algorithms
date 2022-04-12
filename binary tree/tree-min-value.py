# problem:https://structy.net/problems/tree-min-value
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# region bfs iterative
# from collections import deque
#
#
# def tree_min_value(root):
#     queue = deque()
#     queue.append(root)
#     res = None
#     while queue:
#         curr = queue.popleft()
#         if not res:
#             res = curr.val
#         else:
#             if curr.val < res:
#                 res = curr.val
#         if curr.left:
#             queue.append(curr.left)
#         if curr.right:
#             queue.append(curr.right)
#     return res


# endregion


# region dfs recursive
# n = # of nodes
# Time:O(n), Space:O(n)
def tree_min_value(root):
    res = root.val
    if root.left:
        res = min(res, tree_min_value(root.left))
    if root.right:
        res = min(res, tree_min_value(root.right))
    return res


# endregion


if __name__ == '__main__':
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    tree_min_value(a)  # -> -2
