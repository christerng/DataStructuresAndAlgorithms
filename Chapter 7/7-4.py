# Singly linked list O(n)
def swap(L, x, y):
    x_prev = L._head
    while x_prev._next is not x:
        x_prev = x_prev._next

    y_prev = L._head
    while y_prev._next is not y:
        y_prev = y_prev._next

    x._next, y._next = y._next, x._next
    x_prev._next, y_prev._next = y, x

# Doubly linked list O(1)
def swap(L, x, y):
    x_prev = x._prev
    y_prev = y._prev

    x._next, y._next = y._next, x._next
    x_prev._next, y_prev.next = y, x

    x._prev, y._prev = y_prev, x_prev
    x._next._prev, y._next._prev = x, y