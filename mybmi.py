height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")

bmi = int(weight) / float(height) ** 2
bemi = int(bmi)

if bemi <= 18.5:
    print(f"Your BMI is {bemi} , You are underweight.")
elif bemi >=  18.5 and bemi < 25:
    print (f"Your BMI is {bemi} , You have normal weight.")
elif bemi >  25 and bemi < 30:
    print (f"Your BMI is {bemi} , You are overweight.")
elif bemi >  30 and bemi < 35:
    print (f"Your BMI is {bemi} , You are obese.")
else:
    print(f"Your BMI is {bemi} ,You are Clinically Obese.")

