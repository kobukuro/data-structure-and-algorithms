# problem:https://structy.net/problems/get-node-value
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# iterative
# n = number of nodes
# Time:O(n), Space:O(1)
# def get_node_value(head, index):
#     i = 0
#     curr = head
#     while curr is not None:
#         if i == index:
#             return curr.val
#         i += 1
#         curr = curr.next
#     return None

# recursive
# n = number of nodes
# Time:O(n), Space:O(n)
def get_node_value(head, index, i=0):
    if head is None:
        return None
    if i == index:
        return head.val
    return get_node_value(head.next, index, i + 1)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(get_node_value(a, 2))  # 'c'
