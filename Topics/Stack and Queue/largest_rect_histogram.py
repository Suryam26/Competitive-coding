def largest_rectangle_area(heights: list[int]) -> int:
    ans = 0
    n = len(heights)
    stack = []

    for i in range(n + 1):
        while len(stack) and (i == n or heights[stack[-1]] >= heights[i]):
            h = heights[stack[-1]]
            stack.pop()
            if len(stack) == 0:
                w = i
            else:
                w = i - stack[-1] - 1

            ans = max(ans, h * w)

        stack.append(i)

    return ans
