#class Myclass:
#    pass

#mc = Myclass()
#print mc
#<__main__.MyClass instance at 0x7fd1c8d01200>

#这个意思就是说，mc是__main__模块中MyClass来的一个实例（instance），后面的一串十六进制的数字是这个对象的内存地址。


class MyClass:
    name = 'Sam'

    def sayHi(self):
        print 'Hello%s'%self.name

mc = MyClass()
print mc.name
mc.name = 'Lily'
mc.sayHi()


#结果：
#Sam
#HelloLily
