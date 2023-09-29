# 3758_KCPC
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    cnt_team = {}
    scores = [0]*(n+1)
    sub_cnt = [0]*(n+1)

    for j in range(1, n+1):
        cnt_team[j] = {}

    order_time = {}
    for i in range(m):
        a, b, s = map(int, input().split())
        order_time[a] = i
        if b in cnt_team[a].keys():
            if s > cnt_team[a][b]:
                scores[a] -= cnt_team[a][b]
                scores[a] += s
                cnt_team[a][b] = s
        else:
            cnt_team[a][b] = s
            scores[a] += s

        sub_cnt[a] += 1
    answer = []
    ans = 1
    my_score = scores[t]
    for k in range(1, n+1):
        if scores[k] > my_score:
            ans += 1
            max_score = scores[k]
        elif scores[k] == my_score and k != t:
            answer.append(k)
        else:
            continue
    if answer:
        for v in answer:
            if sub_cnt[v] < sub_cnt[t]:
                ans += 1
            elif sub_cnt[v] == sub_cnt[t]:
                if order_time[v] < order_time[t]:
                    ans += 1


    print(ans)
