def find_second_to_last(L):
    node = L._head
    if node is None or node._next is None:
        return -1
    while node._next._next is not None:
        node = node._next
    return node._element