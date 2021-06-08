def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook[:len(phoneBook) - 1], phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

