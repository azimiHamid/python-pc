import random

for i in range(3):
    print(random.random())
    
for i in range(3):
    print(random.randint(20, 40))


members = ["Sarah", "Hamid", "Nabila", "Ali", "Hadi", "Ahmad", "Jamal"]
leader = random.choice(members)
print(leader)