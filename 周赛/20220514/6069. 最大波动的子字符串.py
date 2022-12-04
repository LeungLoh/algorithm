# 字符串的 波动 定义为子字符串中出现次数 最多 的字符次数与出现次数 最少 的字符次数之差。

# 给你一个字符串 s ，它只包含小写英文字母。请你返回 s 里所有 子字符串的 最大波动 值。

# 子字符串 是一个字符串的一段连续字符序列。


# 示例 1：

# 输入：s = "aababbb"
# 输出：3
# 解释：
# 所有可能的波动值和它们对应的子字符串如以下所示：
# - 波动值为 0 的子字符串："a" ，"aa" ，"ab" ，"abab" ，"aababb" ，"ba" ，"b" ，"bb" 和 "bbb" 。
# - 波动值为 1 的子字符串："aab" ，"aba" ，"abb" ，"aabab" ，"ababb" ，"aababbb" 和 "bab" 。
# - 波动值为 2 的子字符串："aaba" ，"ababbb" ，"abbb" 和 "babb" 。
# - 波动值为 3 的子字符串 "babbb" 。
# 所以，最大可能波动值为 3 。
# 示例 2：

# 输入：s = "abcde"
# 输出：0
# 解释：
# s 中没有字母出现超过 1 次，所以 s 中每个子字符串的波动值都是 0 。


class Solution:
    def largestVariance(self, s: str) -> int:
        m = {}
        n = len(s)
        for item in set(s):
            m[item] = [0 for _ in range(n) for _ in range(n)]
        for item in s:


class Solution {
    int a[10005],b[10005],c[10005];
public:
    int largestVariance(string s) {
        int n=s.size(),x,y,i,j,ans=0;
        for(x='a';x<='z';x++){
             for(y='a';y<='z';y++){
                 if(x!=y){
                    for(i=0;i<n;i++)
                        if(s[i]==x)
                            a[i+1]=a[i]+1;
                        else if(s[i]==y)
                            a[i+1]=a[i]-1;
                        else 
                            a[i+1]=a[i];
                    for(i=1;i<=n;i++)
                        b[i]=min(b[i-1],a[i]);
                    for(c[n]=a[n],i=n-1;i;i--)
                        c[i]=max(c[i+1],a[i]);
                    for(i=0;i<n;i++)
                        if(s[i]==y)
                            ans=max(ans,c[i+1]-b[i]);
                }
             }
        }
           
        return ans;
    }
};
