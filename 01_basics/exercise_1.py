weight = float(input("Weight : "))
unit = input("(K)g or (L)bs : ").lower()

if unit == "l":
    weight_in_kg = round(weight * 0.453592, 2)
    print(f"Weight in Kg: {weight_in_kg}")
elif unit == "k":
    weight_in_lbs = round(weight / 0.453592, 2)
    print(f"Weight in Lbs: {weight_in_lbs}")
else:
    print("Wrong unit! Use either 'k' for kg or 'l' for lbs.")


#  kg ≈ 2.20462 lbs
#  lb ≈ 0.453592 kg