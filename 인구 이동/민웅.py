# 16234_인구이동_population movement
import sys
from collections import deque
input = sys.stdin.readline
dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N, L, R = map(int, input().split())

p_lst = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
is_end = True
while True:
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                temp_lst = [[i, j]]
                temp_s = p_lst[i][j]
                temp_c = 1

                while q:
                    x, y = q.popleft()

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]

                        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                            if visited[nx][ny] == 0:
                                if L <= abs(p_lst[x][y]-p_lst[nx][ny]) <= R:
                                    q.append([nx, ny])
                                    visited[nx][ny] = 1
                                    temp_s += p_lst[nx][ny]
                                    temp_c += 1
                                    temp_lst.append([nx, ny])
                if temp_c > 1:
                    is_end = False
                new_popul = int(temp_s/temp_c)
                for c in temp_lst:
                    p_lst[c[0]][c[1]] = new_popul

    if is_end:
        break
    else:
        cnt += 1
        is_end = True

print(cnt)