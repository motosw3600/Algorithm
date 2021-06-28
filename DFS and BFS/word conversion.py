answer = []


def solution(begin, target, words):
    dfs(begin, target, words, [])
    # bfs(begin, target, words)
    return min(answer) if len(answer) > 0 else 0


def bfs(begin, target, words):
    global answer
    visited = []
    queue = [[begin, visited]]
    while queue:
        val = queue.pop()
        if val[0] == target:
            answer.append(len(val[1]))

        for i, word in enumerate(words):
            if diff(val[0], word) == 1 and word not in val[1]:
                queue.append([word, val[1] + [word]])


def dfs(begin, target, words, include):
    global answer
    if begin == target:
        answer.append(len(include))
        return

    elif len(include) == len(words):
        return

    for val in words:
        if val not in include and diff(begin, val) == 1:
            dfs(val, target, words, include + [val])


def diff(word_a, word_b):
    cnt = len(word_a)
    for a, b in zip(word_a, word_b):
        if a == b:
            cnt -= 1

    return cnt


