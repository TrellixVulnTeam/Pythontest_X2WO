from sys import argv

script, filename = argv

txt = open(filename)

print('Here is your file %r' % filename)
print(txt.read())
txt.close()

print('Type the filename again:')
file_again = input('> ')

txt_again = open(file_again, encoding='utf-8')

print(txt_again.readlines())
txt_again.close()

