def job_scheduling(jobs):
    sort_jobs = sorted(jobs, key=lambda x: -x[2])

    n = 0
    for i in sort_jobs:
        n = max(n, i[1])

    ans = [-1] * (n + 1)

    job_count = 0
    max_profit = 0
    for i in range(len(jobs)):
        for j in range(sort_jobs[i][1], 0, -1):
            if ans[j] == -1:
                ans[j] = i
                job_count += 1
                max_profit += sort_jobs[i][2]
                break

    return [job_count, max_profit]


jobs = [[1, 2, 712], [2, 1, 480], [3, 3, 121], [4, 3, 492]]

print(job_scheduling(jobs))
