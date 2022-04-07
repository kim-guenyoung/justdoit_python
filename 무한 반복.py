while (True): #무한루프
    n = int(input('숫자를 입력하세요. 0이면 종료합니다: ')) #정수 입력
    # if (n == 0): #0입력시 무한루프 탈출
    #     break
    print('{} x {} = {}'.format(n, n, n*n))