# Merge Intervals

def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    ans = []
    i = 0
    ans.append(intervals[0])
    for i in range(1, len(intervals)):
        if ans[-1][1] >= intervals[i][0]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])


    return ans


print(merge([[1,3],[2,6],[8,10],[15,18]]))