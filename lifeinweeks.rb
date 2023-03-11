puts "Welcome  Life- In - Weeks program"
puts "What is your current age?"
age = gets.chomp().to_i

max_age = 90
remaining_years = (max_age - age)
no_of_days = (remaining_years) * 365
no_of_weeks = remaining_years * 52
no_of_months = remaining_years * 12


puts   ("You have " + no_of_days.to_s + " days, " + no_of_weeks.to_s + " Weeks, " +  no_of_months.to_s + " Months Left!")
