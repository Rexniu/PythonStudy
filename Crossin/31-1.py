f = file('31-text.txt')
f2 = file('31-text.txt')
f3 = file('31-text.txt')
data = f.read()   
print data
dataline = f2.readline() #读取一行内容
print dataline
datalines = f3.readlines()   #把内容按行读取之一个list中
print datalines
f.close()
