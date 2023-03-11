puts "Enter your height in m: "
height = gets.chomp

puts "Enter your weight in m: "
weight = gets.chomp

bmi = weight.to_i / (height.to_f )** 2
bemi = bmi.to_i 
puts ("Your BMI is " + bemi.to_s)