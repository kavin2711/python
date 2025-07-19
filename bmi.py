def bmi(weight,height):
    return weight / (height ** 2)
weight=int(input("Enter weight in kg: "))
height=float(input("Enter height in meters: "))
print("Your BMI is:", bmi(weight, height))
