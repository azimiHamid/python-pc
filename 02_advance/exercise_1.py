class Person:
    def __init__(self, name):
        self.name = name
        print(name)
        
        
    def talk(self):
        print(f"{self.name} is talking...")
        

person = Person("Hamid")
print(person.name)
person.talk()