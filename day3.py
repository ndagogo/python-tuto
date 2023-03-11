print ("Welcome To the roller Coaster Project!")
height = float(input("what is your height?\n"))


bill = 0
if height >= 120:
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill =5
        print("Child Ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth Ticket is $7")
    elif age >= 45 and age <= 55:
        print ("Everything is gonna be Okay")

    else:
        bill = 12
        print ("Adult Ticket is $12")
    want_photo = input("Do you wana photo? Y or N ?\n")
    if want_photo == "Y":
        my_bill = bill + 3
    print(f"Your total bill is {my_bill}")

else:
    print("You cannot ride")