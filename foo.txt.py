fo= open('foo.txt', 'w')
fo.write('Hello Python!\nI love Python.')
fo.close()

fo= open('foo.txt', 'r')
contents = f.read()
print(contents)
fo.close()