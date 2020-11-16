# 1. 题目地址

 - [英文版题目地址](https://leetcode.com/problems/two-sum/)
 - [中文版题目地址](https://leetcode-cn.com/problems/two-sum/)
# 2. 题目描述
 - **英文描述**

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

 - **中文描述**

```
给定一个整数数组nums和一个目标值target，请你在该数组中找出 和 为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例：

输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
原因：nums[0] + nums[1] = 2 + 7 = 9，所以返回[0, 1]
```
# 3. 解题思路

 - **常规思路**：一般遇到这种题目，我们脑海中最先出现的肯定是**暴力枚举**的方法，暴力进行遍历。也就是使用**两层for循环**来两两遍历每一对元素，从而找出相加符合目标值的两个元素。这样的话：**时间复杂度=O(n^2)**，**空间复杂度=O(1)**
显然，这种暴力遍历、时间复杂度为O(n^2)的方法肯定不是我们想要的最优解法，我们要想办法优化时间复杂度。
 - **优化思路**：保持数组中每个元素与其索引想对应的最好方法就是**哈希表**(HashMap)，即增加一个 Map来记录我们所遍历的数字及其对应的索引值。然后将求和转化为求差，查找 (target-nums[i]) 是否在哈希表中。哈希表是通过以空间来换时间的方法，最优的情况下可以将查找时间从O(n)降低到O(1)。
 - **优化方法一**：**两次遍历的方法，即两次哈希表的方法**
（1）第一次遍历：将每个元素的值和它的索引添加到哈希表中。
 （2）第二次遍历：检查每个元素所对应的目标元素 (target - nums[i]) 是否存在于哈希表中。特别重要的一点是这个目标元素不能是 nums[i] 本身。
 （3）时间复杂度=O(n)，空间复杂度=O(n)
 

```bash
方法一（优化分析）：

 1. 优化主要是利用了哈希表以空间换时间的特性，即最优情况下可以将查找时间从O(n)降低到O(1)。
 2. 将整个数组中的n个元素遍历两次，先将每个元素和索引存表，再遍历查找目标元素是否在表中，所以时间复杂度是O(n)。
 3. 申请的空间即哈希表中所存储的元素数量，存储的数量就是数组中的n个元素，所以空间复杂度为O(n)。
```


 - **优化方法二**：**一次遍历的方法，即遍历的时候一边存表一边查表**
（1）遍历数组中的元素，查询表中是否已经存在当前元素所对应的目标元素 (target-nums[i])，如果存在，那么就已经找到了对应解，立即返回结果，不再往后执行了。如果不存在，那就进行存表的步骤，继续往下遍历查找，直到查询到目标值。
（2）时间复杂度=O(n)，空间复杂度=O(n)

```bash
方法二（优化分析）：

 1. 优化主要是利用了哈希表以空间换时间的特性，即最优情况下可以将查找时间从O(n)降低到O(1)。
 2. 只进行一次遍历操作，遍历的同时在表中查询是否出现过目标元素 (target-nums[i])，如果出现过就立即返回。
 3. 时间复杂度是O(n)，申请的空间取决于哈希表中所存储的元素数量，最多只用存储n个元素，空间复杂度为O(n)。
```

# 4. 解题关键

 - **要想到哈希表的结构，以空间换时间，缩短查询时间为O(1)**
 - **将求和的问题转化为求差值的方法来解决，即：nums[j] = target - nums[i]**
 - **遍历数组中的元素时，边查询边存表，查找到对应解就立即返回结果**
# 5. 示例代码
python

```python
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
    print(result1)
    print("暴力法：", time.perf_counter() - start_1)

    #两次哈希法
    start_2 = time.perf_counter()
    B = Solution2()
    result2 = B.TwoSum(nums, target)
    print(result2)
    print("两次法：", time.perf_counter() - start_2)

    #一次哈希法
    start_3 = time.perf_counter()
    C = Solution3()
    result3 = C.TwoSum(nums, target)
    print(result3)
    print("一次法：", time.perf_counter() - start_3)
```
运行结果

```python
暴力法：
[0, 1]
3.539999999996324e-05
两次法：
[0, 1]
1.6499999999974868e-05
一次法：
[0, 1]
1.3900000000011126e-05
```

