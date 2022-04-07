score = int(input('점수를 입력하세요 : ')) #점수 입력시키기
if (score >= 90): #90점 이상 A
    print('A')
elif(score >= 80): #80점 이상 90점 미만 B
    print('B')
elif(score >= 70): #70점 이상 80점 미만 C
    print('C')
elif(score >= 60): #60점 이상 70점 미만 D
    print('D')
else:
    print('F') #60점 미만 F