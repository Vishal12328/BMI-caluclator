weight_kg = float(input("enter your weight: "))
height_m = float(input("enter your height in m: "))

bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi)

if bmi > 13:
    print("overweight")
else:
    print("you are not overweight")