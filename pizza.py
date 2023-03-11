print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S , M , L\n")
add_pepperoni = input("Do you want  add Pepperoni? Y or N\n")
extra_chesse = input("Do you want extra cheese??\n")


bill =0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
     bill += 2 
    else:
        bill += 3
if extra_chesse == "Y":
    bill +=1
print (f"Your final bill is $ {bill} .")       



