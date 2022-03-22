from re import X


print(1+1)
print(1-2)
print(4/2)
print(int(4/2))

print(float(5))
print(float(1+3))
print(float(5.3))

# x= input('문저열을 입력하세요:')
# print('x')
# a=input("첫 번째 숫자를 입력하세요 :")
# b=input("두 번째 숫자를 입력하세요 :")
# print(a+b)

# a=int(input("첫 번째 숫자를 입력하세요:"))
# b=int(input("두 번째 숫자를 입력하세요:"))
# print(a+b)

# c,d= input('문자열 두 개를 입력하세요:').split()

# print(c)
# print(d)

# e,f = input("숫자  두 개를 입력하세요:").split()
# e= int(e)
# f= int(f)
# print(e+f)

a,b = map(int,input("숫자 두 개를 입력하세요:").split())
print(a+b)