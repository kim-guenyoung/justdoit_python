#file_pointer_test.py
f = open('foo.txt', 'rt')
print('파일 포인터 위치: ', f.tell()) #파일을 연 직후이기 때문에 포인터 값은 0이 될 것이다.
contents1 = f.read()

#file_pointer_test.py
f=open('foo.txt', 'br')
print('파일 포인터 위치: ', f.tell()) # 파일을 연 직후이기 때문에 포인터 값은 0이 될 것이다.
contents1=f.read()