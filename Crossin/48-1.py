#class Myclass:
#    pass

#mc = Myclass()
#print mc
#<__main__.MyClass instance at 0x7fd1c8d01200>

#�����˼����˵��mc��__main__ģ����MyClass����һ��ʵ����instance���������һ��ʮ�����Ƶ����������������ڴ��ַ��


class MyClass:
    name = 'Sam'

    def sayHi(self):
        print 'Hello%s'%self.name

mc = MyClass()
print mc.name
mc.name = 'Lily'
mc.sayHi()


#�����
#Sam
#HelloLily
