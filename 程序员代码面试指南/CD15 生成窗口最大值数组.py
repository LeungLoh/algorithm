"""
描述
有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置，求每一种窗口状态下的最大值。（如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值）
输入描述：
第一行输入n和w，分别代表数组长度和窗口大小
第二行输入n个整数Xi，表示数组中的各个元素
输出描述：
输出一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值
示例1
输入：
8 3
4 3 5 4 3 3 6 7
输出：
5 5 5 4 6 7
说明：
例如，数组为[4，3，5，4，3，3，6，7]，窗口大小为3时：

[4 3 5] 4 3 3 6 7        窗口中最大值为5

4 [3 5 4] 3 3 6 7        窗口中最大值为5

4 3 [5 4 3] 3 6 7        窗口中最大值为5

4 3 5 [4 3 3] 6 7        窗口中最大值为4

4 3 5 4 [3 3 6] 7        窗口中最大值为6

4 3 5 4 3 [3 6 7]        窗口中最大值为7

输出的结果为{5 5 5 4 6 7}
"""


class Solution:
    def getMaxWindowsValue(self, n, arr, w):
        res = []
        windows = []
        for index in range(n):

            while windows and (index - windows[0]) >= w:
                windows.pop(0)

            while windows and arr[windows[-1]] < arr[index]:
                windows.pop()
            windows.append(index)

            if index >= w - 1:
                res.append(arr[windows[0]])
        return res


if __name__ == '__main__':
    n, w = map(int, input().split(' '))
    arr = [int(item) for item in input().split(' ')]
    test = Solution()
    res = [str(item) for item in test.getMaxWindowsValue(n, arr, w)]
    print(" ".join(res))
