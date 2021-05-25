def solution(board, moves):
    answer = 0
    stack = []
    length = len(board)
    for i in moves:
        for j in range(length):
            if sum([board[c][i - 1] for c in range(length)]) == 0:
                break
            if board[j][i - 1] != 0:
                if len(stack) > 0 and stack[-1] == board[j][i - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return answer