def solution(arr):
    answer = [0, 0]

    def quad(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    quad(x, y, n // 2)
                    quad(x + n // 2, y, n // 2)
                    quad(x, y + n // 2, n // 2)
                    quad(x + n // 2, y + n // 2, n // 2)
                    return
        answer[init] += 1

    quad(0, 0, len(arr))
    return answer

