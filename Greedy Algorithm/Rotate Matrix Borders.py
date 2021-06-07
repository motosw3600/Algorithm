def solution(rows, columns, queries):
    answer = []
    n_list = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]
    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        # 2부분으로 나눠서 진행 1. x, y가 nx, ny와 같아질 때 까지 2. nx, ny가 x, y와 같아질 때 까지 돌면서 차 저장
        # +되기전 값을 p로 가지고있음 다음되면 가지고 있던 p를 x+1된 값에다 적용
        re_val = 10000
        p_val = n_list[x1][y1]
        x = x1
        y = y1 + 1
        while x != x1 or y != y1:
            p = n_list[x][y]
            n_list[x][y] = p_val
            re_val = min(re_val, p_val)
            if y < y2 and x == x1:
                y += 1
            elif x < x2 and y == y2:
                x += 1
            elif y > y1 and x == x2:
                y -= 1
            else:
                x -= 1
            p_val = p

        answer.append(re_val)

    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])