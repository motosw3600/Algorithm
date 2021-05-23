#링크와 스타트
#https://www.acmicpc.net/problem/15661
import sys
sys.setrecursionlimit(10**6)
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
team = [False] * (n + 1) #팀의 선택여부
minv=1e9
def dfs(t,d): #선택된 팀의 개수, 트리의 깊이
    global minv
    if d==n:#트리의 깊이는 n=4라면 d==n일때 stop , 끝까지 모든 팀을 본 것이므로
        return
    if t> (int(n//2)+1): #스타트팀과 링크 팀의 차이를 작게하는것이므로, 어느것이 스타트팀인지, 링크팀인지가 중요하지 않다.
        #n의 반정도를 선택하면 나머지것은 자동으로 선택되므로, 1,5의 차이 5,1의 차이는 같아서
        return
    if t>=1: #팀이 하나이상 선택되었다면
        start=link=0
        for i in range(n):
            for j in range(n):
                if team[i]==True and team[j]==True: #2번 3번 팀이 선택된 것이라면,board[2][3]+board[3][2]
                    start+=board[i][j]
                elif team[i]==False and team[j]==False:# 0번 1번이 남았으면, board[0][1]+board[1][0]
                    link+=board[i][j]
        minv=min(abs(start-link),minv)
    #여기서 else: 를 쓰면 안된다. 팀이 하나이상 선택되었든 아니든, 일단 경우의 수를 모두 찾아야 한다.
    team[d]=True
    dfs(t+1,d+1) #팀을 선택한 경우
    team[d]=False
    dfs(t,d+1) #팀을 선택하지 않은 경우
dfs(0,0)
print(minv)