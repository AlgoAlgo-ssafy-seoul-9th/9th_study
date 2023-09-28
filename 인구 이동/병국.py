import math


def bfs(a,b):
    q = [(a, b)]
    tmp = [(a, b)]
    while q:
        x, y = q.pop(0)
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    q.append((nx, ny))
                    v[nx][ny] = 1
                    tmp.append((nx, ny))
    return tmp


N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dir = [[0,1],[1,0],[0,-1],[-1,0]]

answer = 0

while True:
    flag = False
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                v[i][j] = 1
                total = bfs(i,j)
                # total 은 무조건 1개이상이라, >=2 를 해줬어야했음
                if len(total)>=2:
                    flag = True
                    summ = 0
                    for x, y in total:
                        summ += arr[x][y]
                    for x, y in total:
                        arr[x][y] = math.floor(summ/len(total))

    if flag == False:
        print(answer)
        break
    else:
        answer += 1



    # print(q)
    #
    # if q:
    #     summ = 0
    #     for i in range(len(q)):
    #         summ += q[i][2]
    #
    #     for x,y,num in q:
    #         arr[x][y] = math.floor(summ / len(q))
    #     answer += 1
    # else:
    #     print(answer)
    #     break
    #
    #
    #
