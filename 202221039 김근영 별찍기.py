for i in range(5): #세로로 5
   for j in range(5-i-1): #공백 입력
       print(' ', end='')
   for j in range(i*2+1): #2개씩 커지게 별 찍기
       print('*', end='')
   print() #위의 내용 출력하기