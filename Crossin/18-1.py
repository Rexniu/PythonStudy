#在python中，被认为是False的有:
#   为0的数字，包括0.0
#   空字符串，包括‘’，“”
#   表示空值的None
#   空集合，包括(),[],{}
#其他的值都认为是True 
#None是python重的一个特殊值，表示什么都没有，它和0、空字符、False、空集和都不一样。
a = '123'
if a:       #效果相当于if bool(a) 或者 if a !=''
    print 'this is not a blank string'
