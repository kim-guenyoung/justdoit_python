# # from re import T


# # print(type(123))
# # print(type('this'))
# # print(type([1, 2, 3]))
# # print(type((1, 2, 3)))
# # def f(x, y):
# #     return (x+y)
# # print(f)
# # print(type(f))
# # t = f
# # print(t(1, 2))
# # print(f(1, 2))
# # import math
# # print(math)
# # print(type(math))

# # x = [1, 2, 3]
# # print(type(x))
# # x = {1, 2, 3}
# # print(type(x))
# from tkinter import Y


# x = ['this', 'is a', 'book.']
# y = ['this', 'is a', 'book']
# print(id(x), id(y)) #REPL모드의 경우 달라짐. 짧은 단어 같은 경우에는 같을 수도 있긴 함.
# print(id(x[0]), id(y[0]))

# x1 = [1, 2, 3]
# y1 = [1, 2, 3]
# print(id(x1), id(y1))
# x = 1001
# y = 1001
# z = y
# y = 1024
# print(id(x), id(y), id(z))
# x = 'a', 'b'
# print(x)
# x, y = 'a', 'b'
# print('x')

# score = 80
# # if (score > 70):
# #     print('Good Score!')
# # else :
# #     print('Bad Score!')
# score = 80
# if (score > 80):
#     grade = 'A'
# elif (score > 70):
#     grade = 'B'
# elif (score > 60):
#     grade = 'C'
# else:
#     grade = 'D'

# sum = 0
# x = 1
# while (x <= 100):
#     sum = sum + x
#     x = x + 1

# dic1 = {'name' : 'Kim', 'age' : 18, 'height' : 160}
# for key, val in dic1.items():
#     print('{}: {}'.format(key, val))

# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# x = range(1, 10, 1)
# print(x)
# y = range(1, 10000, 1)
# print(list(y))

x = range(0, 20, 2)
x[0:5]
