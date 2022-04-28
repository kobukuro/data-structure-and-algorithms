# problem:https://structy.net/problems/linked-list-find
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# iterative
# n = number of nodes
# Time:O(n), Space:O(1)
# def linked_list_find(head, target):
#     curr = head
#     while curr is not None:
#         if curr.val == target:
#             return True
#         curr = curr.next
#     return False


# recursive
# n = number of nodes
# Time:O(n), Space:O(n)
def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(linked_list_find(a, "c"))  # True
