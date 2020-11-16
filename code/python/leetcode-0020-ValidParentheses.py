# coding:utf-8
'''
# @Method：栈结构
# @Author: wlhr62
'''
import os


class Solution1:
    def isValid(self, s):
        stack = []
        brackets_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        # 遍历字符串
        for x in s:
            if x in brackets_map:  # 如果是左半边括号，压入栈中
                stack.append(x)
            else:  # 如果是右半边括号
                if len(stack):  # 如果栈非空，继续
                    top_element = stack.pop()  # 获取栈顶元素
                    if brackets_map[top_element] != x:  # 如果左右括号不对应，返回False
                        return False
                    else:  # 如果左右括号对应，则继续循环
                        continue
                else:  # 如果栈为空，则返回False
                    return False
        # 遍历完字符串之后，如果有效则栈为空，返回True
        return len(stack) == 0


class Solution2:
    def isValid(self, s):
        while "[]" in s or "()" in s or "{}" in s:
            s = s.replace("[]", "").replace("()", "").replace("{}", "")
        return len(s) == 0


if __name__ == "__main__":
    s1 = "[{}]()"
    s2 = "[{}]("

    A1 = Solution1()
    res1 = A1.isValid(s1)
    print(s1 + ":", res1)
    res2 = A1.isValid(s2)
    print(s2 + ":", res2)

    print("------------------")

    A2 = Solution2()
    res1 = A2.isValid(s1)
    print(s1 + ":", res1)
    res2 = A2.isValid(s2)
    print(s2 + ":", res2)
