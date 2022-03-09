# problem:https://structy.net/problems/tree-includes
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# region dfs iterative
# def tree_includes(root, target):
#     if not root:
#         return False
#
#     stack = [root]
#     while stack:
#         curr = stack.pop()
#         if curr.val == target:
#             return True
#         if curr.left:
#             stack.append(curr.left)
#         if curr.right:
#             stack.append(curr.right)
#     return False
# endregion

# region dfs recursive
# def tree_includes(root, target):
#     if not root:
#         return False
#
#     def dfs(curr):
#         if curr.val == target:
#             return True
#         if curr.left:
#             if dfs(curr.left):
#                 return True
#         if curr.right:
#             if dfs(curr.right):
#                 return True
#         return False
#
#     return dfs(root)
# endregion

# region dfs recursive alvin
def tree_includes(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


# endregion

# region bfs iterative
# n = # of nodes
# Time:O(n), Space:O(n)
# from collections import deque
#
#
# def tree_includes(root, target):
#     if not root:
#         return False
#     queue = deque()
#     queue.append(root)
#     while queue:
#         curr = queue.popleft()
#         if curr.val == target:
#             return True
#         if curr.left:
#             queue.append(curr.left)
#         if curr.right:
#             queue.append(curr.right)
#     return False
# endregion

if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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

    # -> True
    print(tree_includes(a, "e"))
