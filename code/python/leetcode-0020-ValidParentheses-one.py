# coding:utf-8
'''
# @Method：计数器
# @Author: wlhr62
'''
import os


class Solution:
    def isValid(self, s):
        brackets_map = {"(": ")"}
        c = 0
        # 遍历字符串
        for x in s:
            if x in brackets_map:  # 如果是左半边括号，c+1
                c += 1
            else:  # 如果是右半边括号，c-1
                c -= 1
            if c < 0:
                return False
            else:
                continue
        # 遍历完字符串之后，如果有效则c=0，返回True
        return c == 0


if __name__ == "__main__":
    s1 = "()(())"
    s2 = "())"
    A = Solution()
    res1 = A.isValid(s1)
    print(s1 + ":", res1)
    res2 = A.isValid(s2)
    print(s2 + ":", res2)

