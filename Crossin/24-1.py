#������Ҫ����һ������
#���������������һ��ֵx��������һ��ֵy��(x,y)��ʾһ��������ꡣ����Ҫ������������㴦������ϵ����һ�����ޡ�
#x>=0��y>=0�����1��
#x<0��y>=0�����2��
#x<0��y<0�����3��
#x>=0��y<0�����4��

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
                
