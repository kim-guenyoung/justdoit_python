for x in range(3,10): # x= %d단, 3단부터 10단 전까지
    print("{}단을 입력하세요.".format(x))
    for y in range(1, 10): #y= 곱해지는 숫자
        print('{0} * {1} = {2}'.format(x, y, x*y))