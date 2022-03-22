a=1
b=0
for i in range(1,11):
    while a<i:
        if i %a==0:
            b+=1
        a+= 1
    if b==1:
        print(i)
    a=1
    b=0
