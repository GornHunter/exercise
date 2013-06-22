__author__ = 'Nancy'

expr = "3*(1+2)-4*3"
result = "312+*43*-"

op_stack = []


def compute(post_expr):
    for c in post_expr:
        try:
            as_int = int(c)
            op_stack.append(as_int)
        except Exception as e:
            op1 = op_stack.pop()
            op2 = op_stack.pop()

            if c == '+':
                op_stack.append(op1 + op2)
            elif c == '*':
                op_stack.append(op1 * op2)
            elif c == '-':
                op_stack.append(op2 - op1)
            elif c == '/':
                op_stack.append(op2 / op1)
    return op_stack.pop()


def precedence(c):
    if c == '(':
        return 1000
    elif c == '+' or c == '-':
        return 10
    elif c == '*' or c == '/':
        return 20
    elif c == ')':
        return 0


def high_precedence(op1, op2):
    if op1 == '-': op1 = '+'
    if op1 == '/': op1 = '*'
    if op2 == '-': op2 = '+'
    if op2 == '/': op2 = '*'
    table = {
        '+': {'+': '<', '*': '<', '(': '<', ')': '>'},
        '*': {'+': '>', '*': '<', '(': '<', ')': '>'},
        # ( is bigger than anybody
        '(': {'+': '>', '*': '>', '(': '>', ')': '>'},
        # ) is smaller than anybody
        ')': {'+': '<', '*': '<', '(': '<', ')': '<'},
    }
    return table[op1][op2] == '>'


def in2pos(expr):
    result_expr = []
    op_stack = []
    for c in expr:
        if c == ' ':
            continue
        if c in ('+', '-', '(', ')', '*', '/'):
            while len(op_stack):
                top = op_stack[len(op_stack) - 1]
                if high_precedence(c, top):
                    op_stack.append(c)
                    break
                else:
                    if top not in "()":
                        result_expr.append(top)
                    op_stack.pop()
                    # if len(op_stack) == 0:
            op_stack.append(c)
        else:
            result_expr.append(c)

    while len(op_stack) != 0:
        top = op_stack.pop()
        if top not in "()":
            result_expr.append(top)

    return "".join(result_expr)


if __name__ == "__main__":
    tests = [
        ("1*2/4", "12*4/"),
        ("1 + 2 * 3 -4", "123*+4-"),
        ("(3 + 4) * 4", "43+4*"),
        ("1 + 2 * 3", "123*+"),
        ("1*((1 + 3) * 4))", "113+4**")
    ]
    for expr, right in tests:
        if in2pos(expr) != right:
            print("ERROR", expr, '=>', right, "but get:", in2pos(expr))
        else:
            print("OK", expr)

    print(in2pos(expr))

    print(compute(result))