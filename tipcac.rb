puts"Welcome to my tip calculator"

puts "What was the total bill?"
total_bill = gets.chomp().to_f

puts "What percentage tip would you like to give? 10 ,12 ,or 15?"
percentage_tip = gets.chomp().to_i

puts "How many people to split the bill?"
no_of_people = gets.chomp().to_i

   
tip = percentage_tip / 100  * (total_bill)
#actual_pay = tip + total_bill
#final_bill = actual_pay / no_of_people
#main_billa = final_bill
#message= ("Each person should pay $" + tip.to_s)

puts tip
