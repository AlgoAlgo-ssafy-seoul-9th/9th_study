import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n,k,t,m=map(int,input().split())
    board=[[0]*k for _ in range(n)]
    count=[0]*n #제출횟수
    time=[0]*n #제출시간
    for M in range(m):
        i,j,s=map(int,input().split())
        board[i-1][j-1]=max(board[i-1][j-1],s)
        time[i-1]=M
        count[i-1]+=1
    lst=[]
    for idx in range(len(board)):
        lst.append([sum(board[idx]),count[idx],time[idx],idx])
    lst.sort(key=lambda x:(-x[0],x[1],x[2])) # 행의 값 합계를 내림차순으로 정렬하고, 그 다음으로 제출 횟수를 오름차순으로 정렬하며, 마지막으로 제출 시간을 오름차순으로 정렬.
    for idx in range(len(lst)):
        if lst[idx][3]==t-1:
            print(idx+1)
            break