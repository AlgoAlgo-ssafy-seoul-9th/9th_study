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

```

## [병국](<./KCPC/병국.py>)

```py

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
