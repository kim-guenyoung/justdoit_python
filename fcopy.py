fo = open('foo.txt', 'w') #foo.txt 만들기
fo.write('This is line one.\nThis is line two.') #This is line one.
#                                                 This is line two. 만들기
fo.close()
def filecopy(src, dest):  # 함수 만들기
    with open(dest, 'w') as copy:  # 복사본 만들기
        with open(src) as file:  # 복사할 기존 파일 열기
            for line in file:  #모두 복사
                copy.write(line) #텍스트 파일 쓰기, with open으로 열어주었기 때문에 파일 닫아줄 필요 없음
A = input().split()
src = str(A[0]) #복사할 파일 
dest = str(A[1]) #복사한 파일

filecopy(src, dest)  #실행시키기