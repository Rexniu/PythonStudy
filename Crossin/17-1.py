a=1         #python中，可以改变一个变量的类型和值，且定义时不需要加类型明
print a
a='Hello'
print a
a = True
print a     

print '\n'

#print 'Hello' + 1      字符串和整数不能相加
#print 'Hello%d' %'123' %d需要的是一个字符

#int(x) 把x转换成整数
#float(x) 把x转换成浮点数
#str(x) 把x转换成字符串
#bool(x) 把x转换成bool值

print 'Hello'+str(1)
print 'Hello%d' %int('123')

print '\n'

#一些关于bool的式子
print int('123') == 123
print float('3.3') == 3.3
print str(111) == '111'
print bool(0) == False
print bool(-123)
print bool(0)
print bool('abc')
print bool('False')
print bool('')
