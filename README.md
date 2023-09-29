# 9th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/16983)

[코드트리 문제](https://www.codetree.ai/training-field/frequent-problems/problems/go-on-the-rides/description?page=1&pageSize=20&name=%EB%86%80%EC%9D%B4%EA%B8%B0%EA%B5%AC+%ED%83%91%EC%8A%B9)

<br><br>

# 놀이기구 탑승

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./놀이기구 탑승/민웅.py>)

```py
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

```

## [병국](<./놀이기구 탑승/병국.py>)

```py

```

## [상미](<./놀이기구 탑승/상미.py>)

```py

```

## [서희](<./놀이기구 탑승/서희.py>)

```py

```

## [성구](<./놀이기구 탑승/성구.py>)

```py


```

</div>

</details>

<br><br>

# KCPC

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./KCPC/민웅.py>)

```py
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

```

## [병국](<./KCPC/병국.py>)

```py
t = int(input())
# n: 팀 수, k : 문제 수
for _ in range(t):
    n,k,my_team,m = map(int,input().split())
    team_list = [i for i in range(1,n+1)]
    answer_list = [[0]*(k+3) for _ in range(n+1)]
    # 문제3개면 [0,100,50,20, 풀이횟수, 마지막제출시간]
    for i in range(1,m+1):
        id,qnum,score = map(int,input().split())
        answer_list[id][qnum] = max(answer_list[id][qnum],score)
        answer_list[id][k+1] += 1
        answer_list[id][k+2] = max(answer_list[id][k+2],i)

    # print(answer_list)
    my_team_score = sum(answer_list[my_team][:k+1])
    # print(my_team_score)
    my_team_rank = 1
    for i in range(len(answer_list)):
        if sum(answer_list[i][:k+1])>my_team_score:
            my_team_rank+=1
        elif sum(answer_list[i][:k+1])==my_team_score:
            if answer_list[i][k+1] < answer_list[my_team][k+1]:
                my_team_rank+= 1
            elif answer_list[i][k+1] == answer_list[my_team][k+1]:
                if answer_list[i][k+2] < answer_list[my_team][k+2]:
                    my_team_rank += 1
    print(my_team_rank)


```

## [상미](<./KCPC/상미.py>)

```py

```

## [서희](<./KCPC/서희.py>)

```py

```

## [성구](<./KCPC/성구.py>)

```py

```

</div>

</details>

<br><br>

# 인구 이동

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./인구 이동/민웅.py>)

```py

```

## [병국](<./인구 이동/병국.py>)

```py
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


```

## [서희](<./인구 이동/서희.py>)

```py

```

## [성구](<./인구 이동/성구.py>)

```py

```

</div>

</details>

<br><br>

# 로봇 조종하기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./로봇 조종하기/민웅.py>)

```py
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


```

## [병국](<./로봇 조종하기/병국.py>)

```py

```

## [상미](<./로봇 조종하기/상미.py>)

```py

```

## [서희](<./로봇 조종하기/서희.py>)

```py

```

## [성구](<./로봇 조종하기/성구.py>)

```py

```

</div>

</details>

<br><br>
