def count(L):
    node = L._tail._next
    counter = 0
    while node._next is not L._tail._next:
        node = node._next
        counter += 1
    return counter