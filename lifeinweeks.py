print ("Welcome  Life- In - Weeks program")
age = int(input("What is your current age?\n"))

max_age = 100
remaining_years = (max_age - age)
no_of_days = remaining_years * 365
no_of_weeks = remaining_years * 52
no_of_months = remaining_years * 12


print(f" You have {no_of_days} days, {no_of_weeks} weeks and  {no_of_months} months left!")
