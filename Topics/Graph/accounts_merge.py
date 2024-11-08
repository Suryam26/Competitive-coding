from disjoint_set import DisjointSet


def accounts_merge(accounts):
    n = len(accounts)

    ds = DisjointSet(n)

    emails = {}
    for i in range(n):
        for mail in accounts[i][1:]:
            if mail not in emails:
                emails[mail] = i
            else:
                ds.union_by_size(i, emails[mail])

    merged = [[] for _ in range(n)]
    for key in emails:
        idx = ds.find_parent(emails[key])
        merged[idx].append(key)

    ans = []
    for i in range(n):
        row = merged[i]
        if row:
            ans.append([accounts[i][0]] + sorted(row))

    return ans
