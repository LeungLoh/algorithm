#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0
        for nums in dp:
            res += sum(nums)
        for k in range(n,-1,-1):
            for i in range(k):
                j=i+n-k
                if i==j:
                    dp[i][j]=1
                elif s[i]==s[j]:
                    if j-i==1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j-1]
        res=0
        for item in dp:
            res+=sum(item)
            
        return res


# @lc code=end
