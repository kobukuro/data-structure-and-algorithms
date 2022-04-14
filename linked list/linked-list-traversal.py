class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# iterative
# def print_linked_list(head):
#     curr = head
#     while curr:
#         print(curr.val)
#         curr = curr.next

# recursive
def print_linked_list(head):
    if head is None:
        return
    print(head.val)
    print_linked_list(head.next)


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    a.next = b
    b.next = c
    c.next = d

    print_linked_list(a)
