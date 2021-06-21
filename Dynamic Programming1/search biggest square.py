# 내가 처음짠 코드 brute force
# def solution(board):
#     answer = [0]
#     # 완전탐색
#     # board의 가로와 세로 길이 탐색
#     for y in range(len(board)):
#         for x in range(len(board[0])):
#             if board[y][x] == 1:
#                 answer[0] = 1
#                 # boardlen에서 뺀값만큼 for문
#                 min_len = min(len(board[0]) - x, len(board) - y)
#                 if min_len > 1:
#                     for i in range(min_len, 1, -1):
#                         if isSquare(board, x, y, i):
#                             answer.append(i * i)
#                             break
#             else:
#                 continue
#
#     return max(answer)
#
#
# def isSquare(board, x, y, wid):
#     n_list = [board[b][a] for a in range(x, x + wid) for b in range(y, y + wid)]
#     if sum(n_list) == wid * wid:
#         return True
#     else:
#         return False

# dynamic으로 탐색한거 저장해서 풀이(시간복잡도 효율적)
def solution(board):
    answer = []
    row = len(board)
    col = len(board[0])
    for y in range(row):
        for x in range(col):
            if x == 0 or y == 0:
                continue
            if board[y][x] != 0:
                board[y][x] = min(board[y - 1][x - 1], min(board[y - 1][x - 1], board[y][x - 1])) + 1

    for i in range(row):
        answer.append(max(board[i]))

    return max(answer) ** 2