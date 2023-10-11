# 16234 인구이동
import sys
from collections import deque

input = sys.stdin.readline

# 토스트 계란...?

# input
N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    total = country[i][j]
    que = deque([(i, j)])
    event = []
    while que:
        ii, jj = que.popleft()
        for di, dj in dir:
            ni, nj = ii + di, jj + dj
            if (
                0 <= ni < N
                and 0 <= nj < N
                and not visited[ni][nj]
                and L <= abs(country[ii][jj] - country[ni][nj]) <= R
            ):
                visited[ni][nj] = 1
                event.append((ni, nj))
                que.append((ni, nj))
                total += country[ni][nj]
    if len(event):
        event.append((i, j))
        total //= len(event)

        for i, j in event:
            country[i][j] = total
        return 1
    else:
        return 0

for cnt in range(2000):
    visited = [[0] * N for _ in range(N)]
    events = {}
    change = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                change += bfs(i, j)
    if not change:
        print(cnt)
        break
