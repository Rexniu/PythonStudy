#��������������һ�����õ��ܳ��������ٶ���150km/h��Ȼ�����ǳ������A��B��
#��Ҫ��B��C������200km����Ҫ��ֱ�֪�������ֳ���������·����Ҫ����ʱ�䡣
#�������ķ�����
class Car:
    speed = 0
    def drive(self,distance):
        time = distance/self.speed
        print time

car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)
