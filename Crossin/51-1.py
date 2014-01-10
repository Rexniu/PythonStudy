#and or like the bool?a:b in C/C++
a = "heaven"
b = "hell"
c = True and a or b
print c
d = False and a or b
print d

#python的and or语句是利用了python中的逻辑运算实现的。
#当a本身是个假值(如0，“”)时：
a = ""
b = "hell"
c = True and a or b
print c

#and-or真正的技巧在于，确保a的值不会为假。
#最常用的方式是使a成为[a]、b成为[b],然后使用返回值列表的第一个元素

a= ""
b= "hell"
c = (True and [a] or [b])[0]
print c
