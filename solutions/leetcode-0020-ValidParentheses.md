
@[toc]
# 1. 题目地址

 - [英文版题目地址](https://leetcode.com/problems/valid-parentheses/)
 - [中文版题目地址](https://leetcode-cn.com/problems/valid-parentheses/)
# 2. 题目描述
 - **英文描述**

```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

 - **中文描述**

```
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
注意：空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
```
# 3. 解题思路
- **栈结构**：首先想到的就是用**栈**的方法来解决。
（1）使用栈结构，对字符串进行遍历；
（2）如果是左半边括号，则将其压入栈中；
（3）如果是右半边括号，则需要分情况讨论：
   * 如果此时栈为空，则直接return False，结束。
   * 如果此时栈不为空，而且栈顶元素为其对应的左半边括号，则取出栈顶元素，继续进行循环。
   * 如果此时栈不为空，但是栈顶元素不是对应的左半边括号，则直接return False，结束。
 
  （4）时间复杂度：O(n) 【一次遍历】
  （5）空间复杂度：O(n) 【开辟了一个栈空间】

- **正则匹配**
（1）思想：通过不断进行消除"()"、"[]"、"{}"，最后判断剩下的字符串是否是空串即可。
（2）分析：假设s="[{}]\()" 或者 s="\[({})]" 或者 s="{}[]\()"，只要是有效的字符串，最开始必然存在一对相邻的左右对应的括号。因此，必然能够通过s.replace("{}","").replace("[]","").replace("()","")，一步步消除，得到最终的空字符串。
（3）时间复杂度：取决于正则引擎的实现，即replace的实现
（4）空间复杂度：取决于正则引擎的实现，即replace的实现
# 4. 解题关键
- **要想到栈的结构**
    * 时间复杂度：O(n)    【一次遍历】
    * 空间复杂度：O(n)    【开辟了一个栈空间】
- **也可用正则匹配的方式**
   * 时间复杂度：取决于正则引擎的实现
   * 空间复杂度：取决于正则引擎的实现
# 5. 示例代码
python

```python
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
	
```
运行结果

```python
[{}](): True
[{}](: False
------------------
[{}](): True
[{}](: False
```
# 6. 相关题目1
- 如果题目要求只有一种括号，那么可以使用更简洁、更省内存的方式来求解，即**计数器**的方式，而不必要使用栈。
- 如果只有一种括号，设计数器 c = 0：
   * 如果是左括号，那么：c += 1
   * 如果是右括号，那么：c  -= 1
   * 如果 c < 0，直接返回False
   说明出现了有某个右括号提前出现的情况，即"())"或者")"这种情况。
   * 如果 c >= 0，那么继续遍历字符串
   * 遍历完后，c = 0 就说明字符串是有效字符串。
- **示例代码**
python

```python
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
	
```
运行结果

```python
()(()): True
()): False
```

# 7. 相关题目2
leetcode-0032-LongestValidParentheses（最长有效括号）
