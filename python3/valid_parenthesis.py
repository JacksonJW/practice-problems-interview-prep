def isValid(s):
    stack = []
    parens_lookup = {")": "(", "}": "{", "]": "["}
    for paren in s:
        if stack and paren in parens_lookup.keys():
            if parens_lookup[paren] != stack[len(stack)-1]:
                return False
            stack.pop()
        else:
            stack.append(paren)
    return not stack


print("An input of \"()\" yields: " + str(isValid("()")))
print("An input of \"()[]{}\" yields: " + str(isValid("()[]{}")))
print("An input of \"(]\" yields: " + str(isValid("(]")))
print("An input of \"([)]\" yields: " + str(isValid("([)]")))
print("An input of \"{[]}\" yields: " + str(isValid("{[]}")))
