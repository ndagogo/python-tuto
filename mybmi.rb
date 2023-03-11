puts "Enter your height in m: "
height = gets.chomp

puts "Enter your weight in kg: "
weight = gets.chomp

bmi = weight.to_i / (height.to_f )** 2
bemi = bmi.to_i 

if bemi <= 18.5
    puts "Your BMI is " + bemi.to_s + " You are underweight"
elsif bemi >=  18.5 and bemi < 25
    puts "Your BMI is " + bemi.to_s  + " You have normal weight."
elsif bemi >  25 and bemi < 30
    puts "Your BMI is " + bemi.to_s + " You are overweight."
elsif bemi >  30 and bemi < 35
    puts "Your BMI is "  + bemi.to_s + " You are obese."
else
    puts "Your BMI is " + bemi.to_s + " You are Clinically Obese."
end




