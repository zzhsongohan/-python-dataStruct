# class MyStack:
#     def __init__(self):
#         self.queque_in = []
#         self.queque_temp = []
#
#     def push(self, x: int) -> None:
#         self.queque_in.append(x)
#
#     def pop(self) -> int:
#         if self.empty():
#             return None
#         for i in range(len(self.queque_in)-1):
#             self.queque_temp.append(self.queque_in.pop(0))
#         self.queque_in,self.queque_temp = self.queque_temp,self.queque_in
#         return self.queque_temp.pop()
#
#     def top(self) -> int:
#         if self.empty():
#             return None
#         for i in range(len(self.queque_in)-1):
#             self.queque_temp.append(self.queque_in.pop(0))
#         temp_store = self.queque_in(0)
#         self.queque_temp.append(self.queque_in.pop(0))
#         self.queque_in,self.queque_temp = self.queque_temp,self.queque_in
#         return temp_store
#
#     def empty(self) -> bool:
#         return self.queque_in == []

import os
import sys

# 请在此输入您的代码
# my_str = input()
# my_str = my_str.upper()
# temp_str = []
# for i in my_str:
#   if i not in temp_str:
#     temp_str.append(i)
# if len(temp_str) != len(my_str):
#   print("NO")
# else:
#   print("YES")


class Solution:
  def isPalindrome(self, x: int) -> bool:
    s = str(x)
    stack = []
    length = s.length()
    i = 0
    while i<length/2:
      stack.append(s[i])
      i+=1
    if length %2 == 1:
      i+=1
    while i<length:
      if stack.pop() != str[i]:
        return False
    return True




