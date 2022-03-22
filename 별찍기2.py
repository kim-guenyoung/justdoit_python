#for i in range(5):
 #   for j in range(5):
  ##         print('*', end="")
    #        print("", end='*')
    #print


height=int(input()) # 세로
space=height-1 #별들 사이의 빈 공간
for i in range (height): #세로
    for j in range(height+1): #가로
        if j<space:
            print('', end="*")
        else:
            print('*', end='')
    print()