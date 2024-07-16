class Car:
    def __init__(self, name) -> None:
        self.name = name
        
    def start(self):
        print(f"{self.name} is started...")


# pass --> means do nothing 
class Toyota(Car):
    pass 


class Tesla(Car):
    pass


car_1 = Toyota("4Runner")
car_2 = Tesla("Tesla-X")

print(car_1.name)
print(car_2.name)

car_1.start()
car_2.start()