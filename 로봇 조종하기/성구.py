# 2169 로봇 조종하기
# 94128KB 1036 ms
import sys

input = sys.stdin.readline


def solution(N, M, mars):
    dp = [[-1000000001] * M for _ in range(N)]

    dp[0][0] = mars[0][0]

    for i in range(1, M):
        dp[0][i] = dp[0][i - 1] + mars[0][i]

    for i in range(1, N):
        for j in range(M):
            dp[i][j] = dp[i - 1][j] + mars[i][j]
        tmp1 = dp[i].copy()
        for j in range(1, M):
            tmp1[j] = max(tmp1[j], tmp1[j - 1] + mars[i][j])
        tmp2 = dp[i].copy()
        for j in range(M - 2, -1, -1):
            tmp2[j] = max(tmp2[j], tmp2[j + 1] + mars[i][j])
        for j in range(M):
            dp[i][j] = max(tmp1[j], tmp2[j])
    print(dp[-1][-1])


if __name__ == "__main__":
    # input
    N, M = map(int, input().split())

    mars = [list(map(int, input().split())) for _ in range(N)]
    solution(N, M, mars)

"""
def check(k, di):
    return 1 if (di == 0 and k == 1) or (di == 1 and k == 0) else 0


def dfs():
    que = deque([(0, 0, -1)])
    dp = [[-100000001] * M for _ in range(N)]
    # visited = [[0] * M for _ in range(N)]
    dp[0][0] = mars[0][0]
    # visited[0][0] = 1
    while que:
        i, j, di = que.pop()
        for k in range(3):
            ni, nj = i + dir[k][0], j + dir[k][1]
            if (
                0 <= ni < N
                and 0 <= nj < M
                # and not visited[ni][nj]
                and dp[i][j] + mars[ni][nj] > dp[ni][nj]
                and check(k, di)
            ):
                # visited[ni][nj] = 1
                dp[ni][nj] = dp[i][j] + mars[ni][nj]
                que.append((ni, nj, k))
    [print(*dp[t]) for t in range(N)]
    return dp[-1][-1]


print(dfs())
"""
