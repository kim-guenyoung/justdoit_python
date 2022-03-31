import sys
'해피루피.jpg' == sys.argv[0]
f = open('해피루피.jpg', 'rb')
contents = f.read(100)
print(contents)
f.close()