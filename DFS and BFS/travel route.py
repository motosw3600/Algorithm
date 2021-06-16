answer = []
def solution(tickets):
    global answer
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            dfs(tickets, ticket, [idx])

    return sorted(answer)[0]


def dfs(tickets, ticket, waypoint):
    global answer
    if len(waypoint) == len(tickets):
        answer.append([tickets[x][0] for x in waypoint[:-1]] + tickets[waypoint[-1]])

    for i, val in enumerate(tickets):
        if val[0] == ticket[1] and i not in waypoint:
            dfs(tickets, val, waypoint + [i])