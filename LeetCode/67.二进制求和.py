#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c = []
        bit = 0
        flag = False
        while bit < len(a) and bit < len(b):
            v = int(a[bit]) + int(b[bit])
            if flag:
                v += 1
            if v >= 2:
                flag = True
                c.append(str(v - 2))
            else:
                flag = False
                c.append(str(v))
            bit += 1
        if bit < len(a):
            while bit < len(a):
                v = int(a[bit])
                if flag:
                    v += 1
                if v >= 2:
                    flag = True
                    c.append(str(v - 2))
                else:
                    flag = False
                    c.append(str(v))
                bit += 1
        if bit < len(b):
            while bit < len(b):
                v = int(b[bit])
                if flag:
                    v += 1
                if v >= 2:
                    flag = True
                    c.append(str(v - 2))
                else:
                    flag = False
                    c.append(str(v))
                bit += 1
        if flag:
            c.append("1")
        return "".join(c[::-1])


test = Solution()
test.addBinary("11", "1")
# @lc code=end
