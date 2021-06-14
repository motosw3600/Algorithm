from collections import deque
import copy
cnt = 0
def solution(m, n, board):
    # y축은 무조건 깨진 블럭의 높이만큼 추가된다.
    # dfs or bfs로 블록을 탐색하고 깨진블록이 있으면 체크(True or False)
    board = [list(x) for x in board]
    while True:
        c_board = copy.deepcopy(board)
        if c_board == search(board):
            break
        board = search(board)

    return cnt


def search(board):
    # board pop
    board_break = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
    global cnt
    move = [[0, 0], [1, 0], [0, 1], [1, 1]]
    for y in range(len(board) - 1):
        for x in range(len(board[0]) - 1):
            if board[y][x] == 'a':
                continue
            flag = True
            for i in move:
                nx = x + i[0]
                ny = y + i[1]
                if board[y][x] != board[ny][nx]:
                    flag = False
            if flag == True:
                for i in move:
                    if board_break[y + i[1]][x + i[0]] == True:
                        cnt += 1
                    board_break[y + i[1]][x + i[0]] = False

    c_board = copy.deepcopy(board)

    # board settting
    for k in range(len(board[0])):
        n_list = deque([x[k] for x in board_break])
        queue = deque()
        for idx in range(len(n_list)):
            if n_list[idx] == False:
                queue.appendleft(-1)
            else:
                queue.append(idx)

        for i in range(len(queue)):
            if queue[i] == -1:
                board[i][k] = 'a'
            else:
                board[i][k] = c_board[queue[i]][k]

    return board