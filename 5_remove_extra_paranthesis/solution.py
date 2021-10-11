def remove_invalid(eq):
    stack = []
    for i, v in enumerate(eq):
        if v == "(":
            stack.append(v)
        if v == ")":
            if stack == []:
                eq = eq[:i] + eq[i+1:]
            else:
                stack.pop()
    return eq
                

# eq = input()
print(remove_invalid("(ab))cd"))