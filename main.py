# print("hello world")
#
# print(input()+"1234")   # 문자열 연산
#
# if len(input())>10: # 비교 연산
#     print("1234")
#
# for i in range(10): # 반복
#     print(i)
#
# for c in "asdf":    # 반복이 가능한 것은 모두 넣을 수 있습니다
#     print(c+c)
#
# for i in [1, 2, 4, 8, 16]:
#     print(i)
#
# print([2**i for i in range(10)])
#
# for i in range(10):
#     print(i, end=" ")
#
# a=[]
# for i in range(10):
#     a.append(i)
# print(a)
#
# print(a[-1])
# print(a[::-1])
# print(a[1:-1])
# print(a[1:-2:2])
#
# print(input()+input())
# print(int(input())+int(input()))
#
# a, b=map(int, input().split())
# print(a+b)
#
# print(list(map(len, ["a", "as", [1, 2, 3], "asdf"])))
#
# def func(a):
#     return a**2
#
# print(list(map(func, [1, 2, 3])))
#
# print(list(map(lambda x: x**2, [1, 2, 3])))
#



import numpy as np

print(np.array([1, 2, 3]))
print(np.array([[1, 2, 3], [4, 5, 6]]).T)
print(np.array([[1, 2, 3], [4, 5, 6]]).T@[[0, 1], [0, 1]])





