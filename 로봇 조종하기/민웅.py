# 2169_로봇조종하기_controlRobot
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dxy = [(1, 0), (0, 1), (0, -1)]

dp = [[0]*M for _ in range(N)]
planet = [list(map(int, input().split())) for _ in range(N)]

dp[0][0] = planet[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + planet[0][i]

idx = 1
while True:
    if idx == N:
        break

    check1 = [dp[idx-1][i] + planet[idx][i] for i in range(M)]
    check2 = check1.copy()

    for i in range(1, M):
        check1[i] = max(check1[i], check1[i-1]+planet[idx][i])

    for i in range(M-2, -1, -1):
        check2[i] = max(check2[i], check2[i+1]+planet[idx][i])

    for i in range(M):
        dp[idx][i] = max(check2[i], check1[i])

    idx += 1

print(dp[-1][-1])

