# s = 'Python!'

# found = False
# i = 0
# while (True):
#     if (len(s) <= i):
#         break
    
#     if (s[i] == 'x'):
#         found = True
#     i += 1

# print(found)

# s = 'Python!'
# if 'x' in s:
#     print(True)
# else:
#     print(False)

s = 'Python!'
# while(True):
#     if ('x' not in s): #s에 x가 존재하지 않으면 True 출력
#         print(True)
#         break #무한루프 종료
#     else:
#         print(False) # s에 x가 존재하면 False 출력

print(s.find('x')) #출력값이 -1이므로 x는 python이라는 문자열에 존재하지 않는다고 볼 수 있다.