def concatenate(L, M):
    L._trailer._prev._next = M._header._next
    M._header._next._prev = L._trailer._prev
    L._trailer = M._trailer
    L._size += M._size
    return L