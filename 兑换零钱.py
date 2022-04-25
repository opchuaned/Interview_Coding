# Author: Chuan
# Date: 2022/4/25
# Project:

#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
# class Solution:
#     def minMoney(self, arr, aim):
#         # write code here
#         res = []
#         new_arr = sorted(arr, reverse=True)
#         self.find_min(self,new_arr, aim, res)
#         if res and res[-1] == -1:
#             return -1
#         else:
#             return sum(res)
#
#     def find_min(self, arr, aim, res):
#         if aim == 0:
#             return 0
#         if not arr:
#             res.append(-1)
#             return
#         if aim % arr[0] == 0:
#             res.append(aim / arr[0])
#             return
#         else:
#             res.append(aim // arr[0])
#             self.find_min(self,arr[1:], aim % arr[0],res)

class Solution:
    def minMoney(self , arr , aim ):
        # write code here
        if aim < 1:
            return 0
        dp = [(aim+1) for i in range(aim+1)]
        dp[0] = 0
        for i in range(1,aim+1):
            for j in range(len(arr)):
                if arr[j] <= i:
                    dp[i] = min(dp[i],dp[i-arr[j]]+1)
        if dp[aim] > aim:
            return -1
        else:
            return dp[aim]


a = [5,2,3]
b = 20
c = Solution
d = c.minMoney(c,a,b)
print(d)