class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print 'need %f hour(s)' % (distance / self.speed)

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print 'need %f fuels' % (distance * self.fuel)

b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)
#__init__函数会在类被创建的时候自动调用，用来初始化类。
#class定义后面的括号里表示这个类继承于哪个类。
#Car类中，我们又重新定义了__init__和drive函数，这样会覆盖掉它继承自Vehicle的同名函数。但我们依然可以通过“Vehicle.函数名”来调用它的超类方法。
