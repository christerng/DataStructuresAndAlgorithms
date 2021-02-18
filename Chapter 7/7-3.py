def count(L, node=L._head):
    if node is None:
        return 0
    return 1 + count(L, node._next)


"""
    1 + 2 = 3
[1 -> 2 -> 3 -> None]
    1 + 1 = 2
[1 -> 2 -> 3 -> None]
    1 + 0 =1
[1 -> 2 -> 3 -> None]
    0
[1 -> 2 -> 3 -> None]
"""