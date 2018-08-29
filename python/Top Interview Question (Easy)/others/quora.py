from itertools import combinations

def subset_sum(no_of_players,lst, target):
    count = 0
    lst = sorted(lst)
    i = len(lst)-1
    while(i>=0):
        if(lst[0]+lst[i]>target):
            lst.pop()
        else:
            break
        i = i -1


    print lst

    for x in combinations(lst, 3):
        if sum(x) == target:
            count = count +1
    print count

no_of_players = raw_input()
# # print no_of_players
player_score = raw_input()
player_score=list(player_score.split())
player_score =  [int(i) for i in player_score]
# # print player_score
sum_of_Set = int(raw_input())
# # print sum_of_Set
subset_sum(no_of_players,player_score,sum_of_Set)

# (subset_sum(10,[4,5,10,7,3,4,7,4,1,8,21,22],20))