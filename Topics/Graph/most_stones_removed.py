from disjoint_set import DisjointSet


def most_stones_removed(stones):
    n = len(stones)

    row, col = 0, 0
    for r, c in stones:
        row = max(row, r)
        col = max(col, c)

    ds = DisjointSet(row + col + 1)

    stones_set = set()
    for x, y in stones:
        ds.union_by_size(x, y + row + 1)
        stones_set.add(x)
        stones_set.add(y + row + 1)

    count = 0
    for i in stones_set:
        if ds.find_parent(i) == i:
            count += 1

    return n - count
