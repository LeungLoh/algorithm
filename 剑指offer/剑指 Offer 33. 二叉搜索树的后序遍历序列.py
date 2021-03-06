"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
"""


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        index = 0
        length = len(postorder)
        while index < length - 1 and postorder[index] < postorder[-1]:
            index += 1
        for i in range(index, length):
            if postorder[i] < postorder[-1]:
                return False
        return self.verifyPostorder(postorder[:index]) and self.verifyPostorder(postorder[index:-1])
