# Inheritance is used to promotes code reuse and can lead to a more logical and manageable organization of code.

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def walk(self):  # this method is inherited by both cat and mouse
        print(f"{self.name} is walking ...")


class Cat(Animal):
    def __init__(self, name, age, color):  # In a subclass, we usually don't need to define a constructor unless we need to add extra attributes. For example, in the Cat class, a color attribute might be added, which does not exist in the parent Animal class. Other attributes can be inherited from the parent class by using the super() method.
        super().__init__(name, age)
        self.color = color
        
    def makeSound(self):
        print(f"{self.name} is Meowing ...")


class Mouse(Animal):
    def makeSound(self):
        print(f"{self.name} is making some sound...")
        
        
cat = Cat("Tommy", 2, "white")
mouse = Mouse("Jerry", 1)

print(cat.color)

cat.walk()
cat.makeSound()
mouse.walk()
mouse.makeSound()