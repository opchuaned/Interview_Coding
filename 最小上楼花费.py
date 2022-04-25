# Author: Chuan
# Date: 2022/4/25

cost = [1,2,3,4,5]
def minCostClimbingStairs(cost):
    # write code here
    min_cost = []
    for i in range(len(cost)):
        if i == 0:
            min_cost.append(0)
        elif i == 1:
            min_cost.append(0)
        else:
            min_cost.append(min(min_cost[i - 2] + cost[i - 2], min_cost[i - 1] + cost[i - 1]))
    return min(min_cost[-2] + cost[-2], min_cost[-1] + cost[-1])

print(minCostClimbingStairs(cost))