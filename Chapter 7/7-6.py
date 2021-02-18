def same_circular_list(x, y):
    node = x
    while node._next is not y:
        if node._next is x:
            return False
        node = node._next
    return True