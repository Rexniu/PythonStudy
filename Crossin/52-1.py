#元组：
postion = (1,2)
geeks = ('Sheldon','Leonard','Rajesh','Howard')

#元组(tuple)也是一种序列，和用了很多次的list类似。和list有同样的索引、切片、遍历等操作
print postion[0]
for g in geeks:
    print g
print geeks[1:3]

print '%s is %d years old' % ('Mike',23)    #print中用到的元组


#元组作为函数返回值的例子
def get_pos(n):
    return (n/2,n*2)
#得到这个函数的返回值的两种形式
#1.根据返回值元组中元素的个数提供变量
x,y = get_pos(50)
print x
print y

#2.用一个变量记录返回的元组
pos = get_pos(50)
print pos[0]
print pos[1]
