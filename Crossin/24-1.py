#假设需要这样一个程序：
#我们先向程序输入一个值x，再输入一个值y。(x,y)表示一个点的坐标。程序要告诉我们这个点处在坐标系的哪一个象限。
#x>=0，y>=0，输出1；
#x<0，y>=0，输出2；
#x<0，y<0，输出3；
#x>=0，y<0，输出4。

print 'Please input the value of X'
x = input()
print 'Please input the value of Y'
y = input()
if x>=0:
    if y>=0:
        print 1
    else:
            print 4
else:
    if y<0:
        print 3
    else:
        print 2
                
