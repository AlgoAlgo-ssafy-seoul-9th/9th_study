import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
points = [0, 1, 10, 100, 1000]

N = int(input())

liked_lst = [[] for _ in range(N * N + 1)]
mat = [[0] * N for _ in range(N)]
point = 0

for _ in range(N * N):
    num, *liked = list(map(int, input().split()))

    max_cnt = 0
    empty = 0
    ci, cj = 401, 401
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                temp = 0
                now_empty = 0
                for d in dxy:
                    nx = i + d[0]
                    ny = j + d[1]

                    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                        if mat[nx][ny] in liked:
                            temp += 1
                        elif mat[nx][ny] == 0:
                            now_empty += 1

                if temp > max_cnt:
                    empty = now_empty
                    max_cnt = temp
                    ci = i
                    cj = j
                elif temp == max_cnt:
                    if now_empty > empty:
                        empty = now_empty
                        ci = i
                        cj = j
                    elif now_empty == empty:
                        if ci > i:
                            ci = i
                            cj = j
                        elif ci == i:
                            if cj > j:
                                cj = j
    mat[ci][cj] = num
    liked_lst[num] = liked

for i in range(N):
    for j in range(N):
        now = mat[i][j]
        friends = 0
        for d in dxy:
            nx = i + d[0]
            ny = j + d[1]

            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                check = mat[nx][ny]
                if check in liked_lst[now]:
                    friends += 1
        point += points[friends]

print(point)




