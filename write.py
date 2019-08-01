
'''
f = open('newfile.txt', 'a')
f.write("Hello\n")
f.close()
'''

# to write lines 
'''
f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
f.writelines(lines)
f.close()
'''

# to write lines with spaces
f = open('newlines.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()
