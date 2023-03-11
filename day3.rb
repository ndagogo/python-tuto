puts "Welcome To the roller Coaster Project!"
puts "what is your height?"
height = gets.chomp().to_f

if height >= 120
   #puts "You can ride...!"
   puts "What is your age?"
   age = gets.chomp().to_i
   if age <= 12
      puts "You will pay $5"
   elsif age <= 18
     puts "You will pay $7"
   else
    puts "You will pay $12"
        
    end
else
     puts "You cannot ride"
end

puts

gets.chomp()
   