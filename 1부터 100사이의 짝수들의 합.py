# sum = 0 # 합이니까 초기값은 0
# for i in range(2, 101, 2): #2부터 101직전의 공차를. 간격을 2로 설정
#     sum = sum + i # 출력 전 수와 출력될 수를 하나씩 더해가며 100까지 더하기

# print(sum)

sum  = 0 #sum 값 초기화
i = 2 # i = 2 부터 시작
while i <= 100:
    if (i % 2 == 1):
        pass
    else : # 2로 나누어 떨어지는 (=짝수인)
        sum +=i #출력 전 수와 출력될 수를 하나씩 더해가며 100까지 더하기
    
    i = i + 2 #간격은 2로 설정할 것이고

print(sum)