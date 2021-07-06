from collections import defaultdict
def solution(n, edge):
    answer = 0
    n_dic = defaultdict(list)
    node_dis = [-1 for i in range(n)]

    for node in edge:
        n_dic[node[0] - 1].append(node[1] - 1)
        n_dic[node[1] - 1].append(node[0] - 1)

    node_dis[0] = 0
    queue = [0]
    while queue:
        val = queue.pop(0)
        for i in n_dic[val]:
            if node_dis[i] == -1:
                queue.append(i)
                node_dis[i] = node_dis[val] + 1

    node_dis.sort(reverse=True)
    answer = node_dis.count(node_dis[0])
    return answer