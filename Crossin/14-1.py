str1 = 'boring'
str2 = 'day'
num = 18
#print 'My age is'+num   字符和数字不能直接用+相加

print 'My age is '+str(18)  #用str()把数字转化成为字符串
print 'My age is '+str(num)
print 'My age is %d' %num   #用%把数字转化成字符串

print 'Price is %f' %4.99   #%d只能用于整数，小数得用%f

print 'Prince is %.2f' %4.99 #保留两位小数

day = 'Today'
print '%s is a boring day.' %day   #%s代替一段字符串

print '%s is a boring day.' %'Saturday'
