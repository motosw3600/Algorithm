def solution(dirs):
    DELTA = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = 0, 0  # position

    for command in dirs:
        nx, ny = x + DELTA[command][0], y + DELTA[command][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    return len(visited) // 2

solution("LULLLLLLU")


# set을 이용해 visited방문한지 안한지 탐색하면서 확인
# def solution(dirs):
#     answer = 0
#     DELTA = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     visited = set()
#     x, y = 0, 0  # position
#
#     for command in dirs:
#         dx, dy = DELTA[command]
#         nx, ny = x + dx, y + dy
#
#         if nx < -5:
#             nx = -5
#             continue
#         if nx > 5:
#             nx = 5
#             continue
#         if ny < -5:
#             ny = -5
#             continue
#         if ny > 5:
#             ny = 5
#             continue
#
#         go = (x, y, nx, ny)
#         back = (nx, ny, x, y)
#         x, y = nx, ny  # move position
#
#         if go not in visited:
#             visited.add(go)
#             visited.add(back)
#             answer += 1
#
#     return answer
