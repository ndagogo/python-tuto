puts "Welcome To the love calc"

puts ("What is your name?\n").downcase
name1 = gets.chomp()

puts ("What is their name?\n").downcase()
name2 = gets.chomp()

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

op = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

love_score = op.to_s + love.to_s
puts "Your love score is " + love_score.to_s