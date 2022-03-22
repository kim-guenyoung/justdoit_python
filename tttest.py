def prime(num):
    if num==2: #약수 개수가 2개
        return True
    elif num%2==0: #2의 배수 제거
        return False
    else:
        for i in range(3,int(num/2),2):
            if num%i == 0:
                return False
    return True
    
n=int(input('n 입력 '))
for i in range(2,n,1):
    if prime(i):
       print(i)