def solution(expression):
    answer = 0
    operator = [['+', '-', '*'], ['+', '*', '-'],
                ['-', '+', '*'], ['-', '*', '+'],
                ['*', '+', '-'], ['*', '-', '+']]

    for n_list in operator:
        res = int(operate(expression, 0, n_list))
        answer = max(answer, abs(res))
    return answer


def operate(expression, n, oper):
    print(expression, n, oper)
    if n == 2:
        return str(eval(expression))
    if oper[n] == '-':
        res = eval('-'.join([operate(e, n + 1, oper) for e in expression.split('-')]))
    if oper[n] == '+':
        res = eval('+'.join([operate(e, n + 1, oper) for e in expression.split('+')]))
    if oper[n] == '*':
        res = eval('*'.join([operate(e, n + 1, oper) for e in expression.split('*')]))
    return str(res)