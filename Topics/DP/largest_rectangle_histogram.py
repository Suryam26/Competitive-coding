heights = [2, 1, 5, 6, 2, 3]


def largestRectangleArea(heights):
    n = len(heights)
    leftSmaller = [0] * n
    rightSmaller = [0] * n

    stack = []
    for i in range(n):
        while len(stack) and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if len(stack) == 0:
            leftSmaller[i] = 0
        else:
            leftSmaller[i] = stack[-1] + 1

        stack.append(i)

    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if len(stack) == 0:
            rightSmaller[i] = n-1
        else:
            rightSmaller[i] = stack[-1] - 1

        stack.append(i)

    ans = float('-inf')
    for i in range(n):
        area = (rightSmaller[i] - leftSmaller[i] + 1) * heights[i]
        ans = max(ans, area)

    return ans


def largestRectangleArea2(heights):
    ans = 0
    n = len(heights)
    stack = []

    for i in range(n+1):
        while len(stack) and (i == n or heights[stack[-1]] >= heights[i]):
            h = heights[stack[-1]]
            stack.pop()
            if len(stack) == 0:
                w = i
            else:
                w = i - stack[-1] - 1

            ans = max(ans, h*w)

        stack.append(i)

    return ans


# print(largestRectangleArea(heights))
# print(largestRectangleArea2(heights))
