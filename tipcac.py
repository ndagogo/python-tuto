print("Welcome to my tip calculator")

total_bill = float(input("What was the total bill? $\n"))
percentage_tip = int(input("What percentage tip would you like to give? 10 ,12 ,or 15? \n"))
no_of_people = int(input("How many people to split the bill?\n"))
   
tip = (percentage_tip / 100 ) * int(total_bill)
actual_pay = tip + total_bill
final_bill = actual_pay / no_of_people
main_billa = "{:.2f}".format(final_bill)
message= (f"Each person should pay $ {main_billa} ")

print(message)
