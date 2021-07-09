def solution(n, results):
    answer = 0

    graph = [[0 for i in range(n)] for j in range(n)]
    for result in results:
        win = result[0] - 1
        lose = result[1] - 1
        graph[win][lose] = 1
        graph[lose][win] = -1

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if graph[a][b] == 1 and graph[b][c] == 1:
                    graph[a][c] = 1
                    graph[c][a] = -1
                elif graph[a][b] == -1 and graph[b][c] == -1:
                    graph[a][c] = -1
                    graph[c][a] = 1

    for i in range(n):
        if graph[i].count(0) == 1:
            answer += 1

    return answer