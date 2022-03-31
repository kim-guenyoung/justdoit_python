fo = open('해피루피.jpg', 'rb') #'해피루피'라는 jpg파일을 이진 읽기 모드로 연다.
contents = fo.read(100) #100바이트만큼 읽기
print(contents)
fo.close() #파일 닫아주기
