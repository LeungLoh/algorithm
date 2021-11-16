"""
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
"""
Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node == "null":
                    res.append("null")
                    continue
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append("null")
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append("null")
        for i in range(len(res) - 1, -1, -1):
            if res[i] == "null":
                res.pop()
            else:
                break
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == "null":
            return None
        length = len(data)
        root = TreeNode(data[0])
        queue = [root]
        index = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if index < length and data[index] != "null":
                    node.left = TreeNode(data[index])
                    queue.append(node.left)
                index += 1
                if index < length and data[index] != "null":
                    node.right = TreeNode(data[index])
                    queue.append(node.right)
                index += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
