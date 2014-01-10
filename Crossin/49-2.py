#假设我们又有了一辆更好的跑车，它的速度是150km/h，然后我们除了想从A到B，
#还要从B到C（距离200km）。要求分别知道这两种车在这两段路上需要多少时间。
#面向对象的方法：
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
