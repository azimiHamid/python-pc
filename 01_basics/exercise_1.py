weight = float(input("Weight : "))
unit = input("(K)g or (L)bs : ").lower()

if unit == "l":
    weight_in_kg = weight * 0.45
    print(f"weight in Kg : {weight_in_kg}")
elif unit == "k":
    weight_in_lbs = round(weight / 0.45, 2)
    print(f"weight in Lbs : {weight_in_lbs}")
else:
    print("Wrong unit! use wether k for (kg) or l for (lbs)")


#  Kg = 2.22lbs
# lbs = 0.45Kg