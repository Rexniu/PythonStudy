#and or like the bool?a:b in C/C++
a = "heaven"
b = "hell"
c = True and a or b
print c
d = False and a or b
print d

#python��and or�����������python�е��߼�����ʵ�ֵġ�
#��a�����Ǹ���ֵ(��0������)ʱ��
a = ""
b = "hell"
c = True and a or b
print c

#and-or�����ļ������ڣ�ȷ��a��ֵ����Ϊ�١�
#��õķ�ʽ��ʹa��Ϊ[a]��b��Ϊ[b],Ȼ��ʹ�÷���ֵ�б�ĵ�һ��Ԫ��

a= ""
b= "hell"
c = (True and [a] or [b])[0]
print c
