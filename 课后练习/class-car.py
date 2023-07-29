class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        """初始化描述汽车属性"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer_reading(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increase_odometer(self, miles):
        """将里程表增加指定的量"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 80

    def describe_battery(self):
        """打印一条电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " -KWh battery.")

"""
my_used_car = Car("subaru", 'outback', 2013)
my_used_car.get_description()
my_used_car.read_odometer_reading()
my_used_car.update_odometer(1000)
my_used_car.increase_odometer(120)
"""


my_byd = ElectricCar('BYD', 'U8', '2024')
print(my_byd.get_description())
my_byd.describe_battery()
