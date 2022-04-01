# problem:https://structy.net/problems/tree-sum
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# region bfs iterative
# from collections import deque
#
#
# def tree_sum(root):
#     if not root:
#         return 0
#     res = 0
#     queue = deque()
#     queue.append(root)
#     while queue:
#         curr = queue.popleft()
#         res += curr.val
#         if curr.left:
#             queue.append(curr.left)
#         if curr.right:
#             queue.append(curr.right)
#     return res


# endregion

# region dfs recursive
# n = # of nodes
# Time:O(n), Space:O(n)
def tree_sum(root):
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


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

    print(tree_sum(a))  # -> 21
