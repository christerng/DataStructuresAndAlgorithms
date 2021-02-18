def concatenate(L, M):
    node = L._head
    while node._next is not None:
        node = node._next
    node._next = M._head
    L._size += M._size
    return L