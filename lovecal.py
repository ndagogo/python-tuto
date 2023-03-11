print("Welcome To the love calc")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")


t_rue = t + r + u + e
love = l + o + v + e

t_main = str(t_rue)
love_main = str(love)

real = (t_main + love_main )

las= int(real)
#print (f"Your love score is {real}")

if (las < 10 ) or (las > 90 ):
  print(f"You score is {las} , you go together like coke and mentos")
elif (las >= 40) and (las <= 50):
   print  (f"Your score is {las} , you are alright together")
else:
 print (f"Your score is {las}")


