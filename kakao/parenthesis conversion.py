def chkString(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def balance(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = s[:i + 1]
            v = s[i + 1:]
            break
    return u, v

def reverse(s):
    return "".join(['(' if m == ')' else ')' for m in s])

def recursive(s):
    if s == '':
        return ''

    u, v = balance(s)
    print("s:", s,"u:", u,"v", v)
    if chkString(u):
        return u + recursive(v)
    else:
        return '(' + recursive(v) + ')' + reverse(u[1:-1])

def solution(p):
    return p if chkString(p) else recursive(p)

solution("()))((()")