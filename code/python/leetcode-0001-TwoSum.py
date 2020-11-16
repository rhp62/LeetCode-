# -*- coding:utf-8 -*-
'''
# @Method：暴力遍历法 两次哈希法 一次哈希法
# @Author: wlhr62
'''
import time

class Solution1:
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break
                else:
                    continue

class Solution2:
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        for i, num in enumerate(nums):
            minus = target - num
            if minus in hashmap and hashmap[minus] != i:
                return [i, hashmap[minus]]
                break

class Solution3:
    def TwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        for i, num in enumerate(nums):
            minus = target - num
            if minus in hashmap and hashmap[minus] != i:
                return [hashmap[minus], i]
                break
            else:
                hashmap[num] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    #暴力遍历法
    start_1 = time.perf_counter()
    A = Solution1()
    result1 = A.TwoSum(nums, target)
    print("暴力法：")
    print(result1)
    print(time.perf_counter() - start_1)

    #两次哈希法
    start_2 = time.perf_counter()
    B = Solution2()
    result2 = B.TwoSum(nums, target)
    print("两次法：")
    print(result2)
    print(time.perf_counter() - start_2)

    #一次哈希法
    start_3 = time.perf_counter()
    C = Solution3()
    result3 = C.TwoSum(nums, target)
    print("一次法：")
    print(result3)
    print(time.perf_counter() - start_3)