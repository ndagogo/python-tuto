=begin
puts "What is your name?"
name = gets.chomp   
puts ("Hello" + " " + name)
len = name.length()

puts "a: "
a = gets.chomp
puts "b: "
b = gets.chomp

c = a
a = b
b = c

puts("a = " + a)
puts("b = " + b)


#puts "Hello"[1]


puts "What is your name?"
num_char = gets.chomp()
aha = num_char.length()
puts "Your name is "  + aha.to_s + " characters "
=end
 
puts "Type any two numbers:"
two_digit_number = gets.chomp

first_num  = (two_digit_number[0]).to_i
second_num = (two_digit_number[1]).to_i
answ = first_num  + second_num
puts ("Your answer is " + answ.to_s)