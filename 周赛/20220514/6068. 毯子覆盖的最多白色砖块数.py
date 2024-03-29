# 6068. 毯子覆盖的最多白色砖块数 显示英文描述
# 通过的用户数31
# 尝试过的用户数64
# 用户总通过次数32
# 用户总提交次数70
# 题目难度Medium
# 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。

# 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子。

# 请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
import sys


class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        maxnum = 0
        minnum = sys.maxsize

        for tile in tiles:
            maxnum = max(maxnum, tile[1])
            minnum = min(minnum, tile[0])
        print(maxnum)
        print(minnum)
        bitmap = [0] * (maxnum + 1)
        for tile in tiles:
            bitmap[tile[0]: tile[1] + 1] = [1 for _ in range(tile[1] - tile[0] + 1)]
        if carpetLen >= maxnum:
            return sum(bitmap)

        dp = [0] * (len(bitmap) - carpetLen - 1)
        dp[0] = sum(bitmap[:carpetLen + 1])

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] - bitmap[i] + bitmap[i + carpetLen + 1]
        return max(dp)


test = Solution()
print(test.maximumWhiteTiles([[3745, 3757], [3663, 3681], [3593, 3605], [3890, 3903], [3529, 3539], [3684, 3686], [3023, 3026], [2551, 2569], [3776, 3789], [3243, 3256], [3477, 3497], [2650, 2654], [2264, 2266], [2582, 2599], [2846, 2863], [2346, 2364], [3839, 3842], [3926, 3935], [2995, 3012], [3152, 3167], [4133, 4134], [4048, 4058], [3719, 3730], [2498, 2510], [2277, 2295], [4117, 4128], [3043, 3054], [3394, 3402], [3921, 3924], [3500, 3514], [2789, 2808], [3291, 3294], [2873, 2881], [2760, 2760], [3349, 3362], [2888, 2899], [3802, 3822], [3540, 3542], [3128, 3142], [2617, 2632], [3979, 3994], [2780, 2781], [
      3213, 3233], [3099, 3113], [3646, 3651], [3956, 3963], [2674, 2691], [3860, 3873], [3363, 3370], [2727, 2737], [2453, 2471], [4011, 4031], [3566, 3577], [2705, 2707], [3560, 3565], [3454, 3456], [3655, 3660], [4100, 4103], [2382, 2382], [4032, 4033], [2518, 2531], [2739, 2749], [3067, 3079], [4068, 4074], [2297, 2312], [2489, 2490], [2954, 2974], [2400, 2418], [3271, 3272], [3628, 3632], [3372, 3377], [2920, 2940], [3315, 3330], [3417, 3435], [4146, 4156], [2324, 2340], [2426, 2435], [2373, 2376], [3621, 3626], [2826, 2832], [3937, 3949], [3178, 3195], [4081, 4082], [4092, 4098], [3688, 3698]], 1638))
