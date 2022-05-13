class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# iterative
# n = number of nodes
# Time:O(n), Space:O(1)
# Space complexity is constant, because we only need a fixed number of variables.
# def reverse_list(head):
#     prev, curr = None, head
#     while curr is not None:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev

# recursive
# n = number of nodes
# Time:O(n), Space:O(n)
def reverse_list(head, prev=None):
    if head is None:
        return prev
    nxt = head.next
    head.next = prev
    return reverse_list(nxt, head)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    reverse_list(a)  # f -> e -> d -> c -> b -> a
