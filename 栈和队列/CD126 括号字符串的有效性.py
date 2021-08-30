"""
描述
给定一个字符串str，判断是不是整体有效的括号字符串(整体有效：即存在一种括号匹配方案，使每个括号字符均能找到对应的反向括号，且字符串中不包含非括号字符)。
输入描述：
输入包含一行，代表str。
输出描述：
输出一行，如果str是整体有效的括号字符串，请输出“YES”，否则输出“NO”。
示例1
输入：
(()) 
输出：
YES 
复制
示例2
输入：
()a() 
输出：
NO 
说明：
()a()中包含了 ‘a’，a不是括号字符
"""


class Solution:
    def checkbrackets(self, arr):
        res = []

        for item in arr:
            if item != ')':
                res.append(item)
            else:
                while res and res[-1] != '(':
                    res.pop()
                if not res:
                    print("NO")
                    return
                res.pop()
        if res:
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    s = input()
    test = Solution()
    test.checkbrackets(s)
