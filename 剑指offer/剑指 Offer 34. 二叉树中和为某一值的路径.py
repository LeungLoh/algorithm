"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

 

示例 1：



输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：



输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = []

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.dfs(root, [], 0, target)
        return self.res

    def dfs(self, root, temp, total, target):
        if not root:
            return
        if not root.left and not root.right:
            if total + root.val == target:
                temp.append(root.val)
                self.res.append(temp)
                return
        if root.left:
            self.dfs(root.left, temp + [root.val], total + root.val, target)
        if root.right:
            self.dfs(root.right, temp + [root.val], total + root.val, target)
