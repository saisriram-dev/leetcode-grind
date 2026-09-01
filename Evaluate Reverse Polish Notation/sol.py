def evalRPN(tokens):
    stack = []

    for token in tokens:
        try:
            val = int(token)
            stack.append(val)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack[-1]
