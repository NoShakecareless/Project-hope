class Restaurant():
    # 这是一个餐馆的类实例
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        """"这是一个测试样例"""
        restaurant_name = str(self.name)
        cuisine_type = str(self.type)
        print("This is a " + restaurant_name + " and its type is " + cuisine_type + ".")

    def open_restaurant(self):
        print(self.name + " is open!")

    def set_number_served(self, num):
        self.number_served = num

    def increase_number_served(self, nums):
        self.number_served += nums

    def show_number_served(self):
        print("This restaurant has served " + str(self.number_served) + " customers today")


class User():
    # 这是实例化的第二部分
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Name is " + full_name)

    def greet_user(self):
        print("Welcome " + self.first_name + '.' + self.last_name + "!")


my_restaurant = Restaurant("好吃不上火", "Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_info = User('David', 'Bland')
my_info.describe_user()
my_info.greet_user()
my_restaurant.show_number_served()
my_restaurant.set_number_served(18)
my_restaurant.show_number_served()
my_restaurant.increase_number_served(100)
my_restaurant.show_number_served()
