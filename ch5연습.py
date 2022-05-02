# v = 'expr'
# print(type('obj'))
# print(type(123))
# print(type(12.3))
# print(type('this'))
# print(type([1, 2, 3]))
# print(type((1, 2, 3)))
# print(type({'name' : 'kim', 'age' : '20'}))
# def f(x, y):
#     return (x+y)

# print(type(f))

# import math
# print(type(math))

# import math
# print(f'the value of pi is approximately {math.pi:.4f}.')



# print(1 == 1.0) # 값이 같으니까 True
# print(1 is 1.0) # 정수와 실수라는 점에서 차이가 있으니 False

# x = 1; y = 1.0
# print(id(x), id(y)) #참조 값이 다르니 주소도 다르게 출력될 것임
# print(id(x) == id(y)) #False

# z = 1; w = z
# print(id(z), id(w)) #동일한 객체이니 주소가 같게 출력될 것임
# print(id(z) == id(w)) #True

# score = 80
# if (score >70):
#     print('Good Score!')
# else : 
#     print('Bad Score')

# sum = 0
# x = 2
# while (x <= 100):
#     sum += x
#     x += 2 #짝수 합// 만약에 x+=1 1~100까지 더하는 코드

# print(sum)

# sum = 0
# x = 1
# while True:
#     sum += x
#     x += 1
#     print(sum) #무한반복
#     if (x>=100):
#         break

# i = int(input('정수 : '))
# t = 1; r=1

# while (t <= i):
#     r = r * t
#     t = t + 1

# print('factorial({}) = {}'.format(i,r))

# score_list = [77, 87, 65, 98]
# for x in score_list:
#     print(x)


#sum = 0
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum += i

# print(sum)

# for x in range(1, 11):
#     sum += x
# print(sum) 

# dic1 = {'name' : 'KimGuenyoung', 'age': 20, 'height' : 180}
# for key, val in dic1.items():
#     print('{}: {}'.format(key, val))


# elements = [0, 200, 50,25, 10, 255]
# values = bytearray(elements)
# print(values)

# values[0]= 5
# values[1] = 0
# print(values[0])
# print(values[1])

# data = bytearray(b'abc')
# print(data)
# print(data[0])
# print(data[1])
# data.append(250)
# print(data)

# for c in 'This':
#     print(c)

# sum = 0
# for i in range(1, 101):
#     sum += i

# print(sum)

# r1 = range(0, 10)
# print(type(r1))
# print(tuple(r1))
# print(list(r1))
# print(set(r1))
# print(dict(r1))

# r = range(0, 20, 2)

# print(list(r))
# print(11 in r)
# print(10 in r)

# print(r.index(10))

# print(r[5])

# print(r[0:5])

# print(r[-1])

# print('%10o'%43)
# print('%10.3e' %123.45678)

# pi = 3.1415926535
# print('{0:3.2f}'.format(pi))

# print('{0: <20s} {1:6.2f}'.format('Spam & Eggs:', 6.99))

# x = 1; y = 2; z = 3
# print(f'x + y = {x + y}')
# print('x + y * z = %d' % (x + y * z))

# animals = 'cats'
# print(f'I love {animals}.')

# import os
# os.remove('in.txt')

# import os
# os.mkdir('test')

# import os
# os.rmdir('test')


# fo  = open('foo.txt', 'w')
# contents = fo.read(100)
# print('contents : ', contents)
# fo.close()

# import os
# os.rmdir('foo.txt')

# f = open('foo.txt', 'wt')
# f.write('This is line one.\nThis is line two.\nPython is great!\n')
# f.close()

# f = open('foo.txt', 'rt')
# print('파일 포인터 위치 : ', f.tell())
# contents = f.read()

# print('파일 포인터 위치 : ', f.tell())
# contents2 = f.read()
# print('contents1 : [{}]\n'.format(contents2))

# f.seek(0) #다시 0으로
# print('파일 포인터 위치 : ', f.tell())
# contents3 = f.read()
# print('contents3 : [{}]\n'.format(contents3))

# import sys
# sys.stdin = open('C:\Users\김근영\source\혼자 공부하는 python\in.txt', 'r')
# input(Hello)


# import sys

# if (len(sys.argv) != 3):
#     print('Usage: python fcopy <src.txt> <dest.txt>')
#     sys.exit()

# src = open(sys.argv[1], 'tr')
# c = src.read()
# print(c)

# dest = open(sys.argv[2], 'tw')
# dest.write(c)
# src.close()
# dest.close()

# def sum(x, y):
#     '이 함수는 x와 y의 합을 반환한다.'
#     sum = x + y
#     return sum

# i = int(input('정수 : '))
# t = 1; r = 1

# while (t <= i):
#     r = r * t
#     t = t + 1
# print('{}! = {}'.format(i, r))

# sum = 0
# for x in range(1, 11):
#     sum += x

# print(sum)

# sum = 0
# i = int(input('정수 : '))
# for i in range(1, i + 1):
#     sum = sum + i

# print(sum)

# dic1 = {'name' : 'Kim', 'age' : 18, 'height' : 160}
# for key, val in dic1.items():
    # print('{} : {}'.format(key, val))

# factorial = 1
# i = int(input('자연수 : '))
# for i in range(1, i+1):
#     factorial *= i
    
# print('{}! = {}'.format(i, factorial))


# i = int(input('자연수 : '))
# t = 1
# r = 1
# while (t <= i):
#     r = r * t
#     t = t + 1

# print('factorial({}) = {}'.format(i , r))

# i = 1
# while(i <= 100):
#     i = i + 1
#     if((i % 7 != 0)):
#         continue
#     else:
#         print(i)

# def factorial(n):
#     if (n == 0):
#         return 1
#     else:
#         return(print(n * factorial(n-1)))

# def factorial(n):
#     return (1 if (n == 0) else (n * factorial(n-1)))

# for _ in range(0, 3):
#     print('hello')

# a, *b, c = [1, 2, 3, 4, 5]
# print(a)
# print(b)

# x = [1, 2, 3]
# x0, x1, x2 = x
# print(x0, x1, x2)

# def g(name, age, addr):
#     print(name, age, addr)
# t1 = ('Kim', 23, 'Seoul')
# print(g(*t1))
# g('Kim', 23, 'Seoul')
# print(g)
# t2 = ['park', 25, 'Cheonan']
# print(*t2)

# def point(x, y):
#     print('({}, {})'.format(x, y))

# p1 = {'x': 1, 'y' : 2}
# print(point(**p1))

# def f(x, y, /, z):
#     print(x, y, z)

# def calc(a, b, c = 0, d = 0):
#     return (a - b + c - d)

# print(calc(1, 2, 3, 4))
# print(calc(a= 1, b =2, c = 3, d = 4))
# print(calc(1, 2, 3))

# def swap(x, y):
#     temp = x
#     x = y
#     y = temp

# a = 50
# b = 100
# print(a, b)
# swap(a, b)
# print(a, b)

# def range_sum(x):
#     sum_x = 0
#     for c in range(x+1):
#         sum_x += c
    
#     return sum_x

# print(range_sum(10))
# print(sum_x)

# class X:
#     def range_sum(self, x):
#         sum_x = 0
#         for c in range(x + 1):
#             sum_x = sum_x + c

#         return sum_x
    
# x1 = X()
# # print(x1.range_sum(10))

# x = 100

# def f(m):
#     print('x =', x)
#     return x * m

# def g():
#     x = 200
#     print('x = ', x)
#     return X

# print(g())
# print(f(5))

# a = 'Hello, world!\n'
# print(a*2)

# print('Hello, world!\n'*2)



# def commons (x, y):
#     x = [6, 1, 4, 3, 4, 5]
#     y = [7, 4, 5, 7, 8]
#     z = x & y
#     return z

# print(commons(x & y))

# # 소수 판정
# num = int(input('2 이상의 정수 입력 : '))

# is_prime = True;
# for i in range(2, num):
#     if ((num % i) == 0):
#         print('{} = {} x {}이므로'.format(num, i, int(num/i)))
#         is_prime = False
#         break
# if (is_prime):
#     print('{}은(는) 소수입니다.'.format(num))
# else:
#     print('{}은(는) 소수가 아닙니다.'.format(num))

# def commons(x, y):
#     result = []
    
#     if len(x) >= len(y):
#         tmp = x
#         tmp2 = y
#     else:
#         tmp = y
#         tmp2 = x

#     for i in tmp:
#         if i in tmp2:
#             result.append(i)

#         else:
#             pass
        
# def add_number(n1, n2):
#     ret = n1 + n2
#     return ret

# def add_txt(t1, t2):
#     print(t1 + t2)

# ans = add_number(10, 15)
# print(ans)
# text1 = '대한민국'
# text2 = '만세!'
# add_txt(text1, text2)

# def add_txt(t1, t2= '파이썬'):
#     print(t1 + ':' + t2)

# add_txt('베스트')
# add_txt(t2 = '대한민국', t1 = '1등')

# def func1(*args):
#     print(args)

# def func2(width, height, **kwargs):
#     print(kwargs)

# func1()
# func1(3, 5, 1, 5)
# func2(10, 20)
# func2(10, 20, depth = 50, color = 'blue')


# param = 10
# strdata = '전역변수'

# def func1():
#     strdata = '지역변수'
#     print(strdata)

# def func2(param):
#     param = 1

# def func3():
#     global param
#     param = 50

# func1() #지역변수
# print(strdata) #전역변수
# print(param) #10
# func2(param) #지역변수니까 유효하지 않음
# print(param) #10이 출력됨
# func3()  #func3은 전역변수 param의 값을 변경하는 것임
# print(param) #따라서 전역변수 param 값을 출력하면 50이 됨

# def reverse(x, y, z):
#     return z, y, x

# ret = reverse(1, 2, 3)
# print(ret)

# r1, r2, r3 = reverse('a', 'b', 'c')
# print(r1); print(r2); print(r3)

# b1 = bin(97)
# print(b1)
# b2 = bin(98)
# print(b2)
# ret1 = (b1 + b2)
# print(ret1)
# a = int(b1, 2)
# print(a)
# b = int(b2, 2) #2진수라는 뜻

# ret2 = a + b
# print(hex(ret2))

# x = [6, 1, 4, 3, 4, 5]
# y = [7, 4, 5, 7, 8]

# def commons(x, y):
#     x_set = set(x)
#     y_set = set(y)
#     z = []
#     for i in x_set:
#         if i in y_set:
#             z.append(i)
#     z.sort()
#     return z
# print(set(commons(x, y)))


# def sum_of_multiples_of(n):
#     if (n != 5):
#         return 1
#     else:
#         return n + n


# if condition:
#     x = true_value
# else:
#     x = false_value

# 이걸 조건수식으로 바꾸어 보면
# true_value if condition else false_Value

# def max2(x, y):
#     if (x > y):
#         return x
#     else:
#         return y
# 조건 수식으로 바꾸어보면
# def max2(x, y):
#     return (x if (x > y) else y)

# def factorial(n):
#     if (n == 0):
#         return 1
#     else:
#         return (n * factorial(n-1))
# 조건 수식으로 바꾸어보면
# def factorial(n):
#     return (1 if (n == 0) else (n * factorial(n-1)))

# def point(x, y):
#     print('({}, {})'.format(x, y))

# p1 = {'x': 1, 'y': 2}
# point(**p1)
# point(x = 1, y = 2)
# p2 = {'y' : 3, 'x' : 5}
# point(**p2)
# point(x = 5, y = 3)

# def foo(arg1, arg2, /):
#     print(arg1, arg2)
# def foo2(*args):
#     print(args)
# print(foo(1, 2))

# def swap(x, y):
#     temp = x
#     x = y
#     y = temp

# a = 100
# b = 200
# print(a, b)
# swap(a, b)
# print(a, b)

# i = int(input('정수 입력 : '))
# t = 1; r =1
# while(t <= i):
#     r = r * t
#     t = t + 1
# print('{}! = {}'.format(i, r))

# factorial = 1
# for i in range(1, i + 1):
#     factorial = factorial * i
# print('{}! = {}'.format(i, factorial))

# r = [x * x for x in [1, 2, 3, 4, 5]]
# print(r)

# numbers = [22, 13, 45, 98, 50, 29, 43, 44 , 1]
# print([x for x in numbers if x > 45])

# colors = ['red', 'green', 'yellow', 'blue']
# things = ['house', 'can', 'tree']
# colored_things = [(x, y) for x in colors for y in things]
# print(colored_things)

# numbers = [22, 13, 45, 50, 98, 69, 43, 44, 1]
# x = 10
# print(x + 1 if x >= 45 else x + 5)
# print([x + 1 if x >= 45 else x + 5 for x in numbers])

print([x*x for x in range(10)])