# problem:https://structy.net/problems/max-root-to-leaf-path-sum
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# region dfs recursive
# n = # of nodes
# Time:O(n), Space:O(n)
def max_path_sum(root):
    number = root.val
    compare = []
    if root.left:
        compare.append(max_path_sum(root.left))
    if root.right:
        compare.append(max_path_sum(root.right))
    return number + max(compare) if compare else number


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

    print(max_path_sum(a))  # -> 18
