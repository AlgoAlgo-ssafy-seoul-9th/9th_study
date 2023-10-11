# from collections import deque

# N, L, R = map(int, input().split())

# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input().split())))

# visited = [
#     [False for _ in range(N)]
#     for _ in range(N)
# ]

# q = deque()

# def in_range(x, y):
#     return 0 <= x and x < N and 0 <= y and y < N

# def can_go(x, y):
#     return in_range(x, y) and arr[x][y] and not visited[x][y]


# def bfs():
#     while q:
#         x, y = q.popleft()
#         dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
#         for dx, dy in zip(dxs, dys):
#             nx, ny = x + dx, y + dy
#             if 0 <= nx and nx < N and 0 <= ny and ny and N:
                
    

    
# dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

# for i in range(N):
#     stack = []
#     for j in range(N):
#         for di, dj in zip(dxs, dys):
#             nx, ny = i + di, j + dj
#             if 0 <= nx and nx < N and 0 <= ny and ny and N:




import sys
import math
from collections import deque

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]


input = sys.stdin.readline()

n, l, r = map(int, input().split())

arr = list()
a_list = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    count = arr[i][j]   # 총 연합된 국가 수 
        # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기 
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dxs[d]
            ny = y + dys[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기 
                union.append((nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))
                count += arr[nx][ny]
    # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산  
    for x, y in union:
        arr[x][y] = math.floor(count / len(union))

    return len(union)

result = 0    # 인구 이동이 발생하는 일수 
while True:   # 1. 인구 이동이 없을 때까지 반복 
    visited = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동 존재 유무 플래그 
    # 2. 모든 곳을 bfs로 방문하여 연합 진행 
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:   # 3. 지금까지 인구 이동이 없는 경우, 그만 
        break
    result += 1

print(result)