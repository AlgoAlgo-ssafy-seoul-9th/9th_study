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

