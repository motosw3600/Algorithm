def solution(n, words):
    s = [words[0]]
    idx = 0
    for i, word in enumerate(words[1:]):
        if s[-1][-1] != word[0] or word in s:
            idx = i + 1
            break
        s.append(word)

    return [(idx % n) + 1, (idx // n) + 1] if idx != 0 else [0, 0]