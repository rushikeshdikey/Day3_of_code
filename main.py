# start to python day-3 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 06-03-2022

# BMI Calculator

print("Welcome to BMI calculator")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kgs: "))

# h = float(height)
# w = float(weight)

bmi = round(weight / height ** 2)

#print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print(f"Your BMI is: {bmi}, you are Under weight.")
elif bmi < 25:
    print(f"Your BMI is: {bmi}, you are Normal weight.")
elif bmi < 30:
    print(f"Your BMI is: {bmi}, you are Over weight.")
else:
    print(f"Your BMI is: {bmi}, are Obese")