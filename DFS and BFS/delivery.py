from collections import defaultdict
from collections import deque

# Dijkstra Algorithm
def solution(N, road, K):
    answer = [1]

    n_dic = defaultdict(list)
    delivery_time = {}
    for i in range(1, N + 1):
        delivery_time[i] = K + 1

    for val in road:
        n_dic[val[0]].append(val[1:])
        n_dic[val[1]].append([val[0], val[2]])

    queue = deque([[1, 0]])
    while queue:
        data = queue.popleft()
        home = data[0]
        time = data[1]
        for homes in n_dic[home]:
            if time + homes[1] <= K and time + homes[1] < delivery_time[homes[0]]:
                answer.append(homes[0])
                delivery_time[homes[0]] = time + homes[1]
                queue.append([homes[0], time + homes[1]])
            else:
                continue

    return len(set(answer))