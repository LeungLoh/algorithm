#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        delnode, parent = self.find(root, key, None)
        if not delnode:
            return root
        if not parent:
            if not delnode.left:
                return delnode.right
            elif not delnode.right:
                return delnode.left
            left, pre = self.findmaxleft(delnode.right)
            if pre:
                pre.left = left.right
                left.left = delnode.left
                left.right = delnode.right
            else:
                left.left = delnode.left
            return left

        left, pre = self.findmaxleft(delnode.right)
        if not left:
            if parent.left and parent.left.val == delnode.val:
                parent.left = delnode.left
            else:
                parent.right = delnode.left
        else:
            if pre:
                pre.left = left.right
                left.left = delnode.left
                left.right = delnode.right
            else:
                left.left = delnode.left

            if parent.left and parent.left.val == delnode.val:
                parent.left = left
            else:
                parent.right = left
            delnode.left = None
            delnode.right = None
        return root

    def findmaxleft(self, root):
        if not root:
            return None, None
        pre = None
        while root.left:
            pre = root
            root = root.left
        return root, pre

    def find(self, root, key, parent):
        if not root:
            return None, parent
        if root.val > key:
            return self.find(root.left, key, root)
        if root.val < key:
            return self.find(root.right, key, root)
        if root.val == key:
            return root, parent
# @lc code=end
