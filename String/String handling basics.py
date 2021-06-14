def solution(s):
    try:
        int(s)
    except:
        return False
    return s.isdigit()

    # return len(s) in (4, 6) and s.isdigit()