import sys

if (len(sys.argv) !=3):
    print('C: python> python calc.py <a> <b> <c>')
    sys.exit(1)
else:
    a = int(sys.argv[1])  #명령행인자 <a>를 가리킴
    b = sys.argv[2]  #명령행인자 <b>를 가리킴
    c = int(sys.argv[3])  #명령행인자 <c>를 가리킴
    if b == '+':  #b에 + 입력 시 더하기
        print(int(a)+int(c))
    elif b == '-':  #b에 - 입력시 빼기
        print(int(a)-int(c))
    elif b == 'x':  #b에 * 입력 시 곱하기
        print(int(a)*int(c))
    elif b == '/':  #b에 / 입력 시 나누기/// 나누었을 때 실수형으로 나오기 때문에 한번 더 int로 변환해야함
        print(int(int(a)/int(c)))
