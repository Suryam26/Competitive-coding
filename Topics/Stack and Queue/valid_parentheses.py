# Link: https://leetcode.com/problems/valid-parentheses/submissions/

def is_valid(s):
    stack = []
    d = {'(': ')', '[': ']', '{': '}'}

    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if not len(stack):
                return False
            if i != d[stack.pop()]:
                return False

    if len(stack):
        return False
    return True


print(is_valid('[](){'))
