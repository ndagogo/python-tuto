import random

#states = ["Minnesota" , "Oregon" , "Kansas" , "West Virginia" , "Nevada" ,  "Nebraska" , "Colorado" , "North Dakota" ,"South Dakota" , "Montana" , "Washington" , "Idaho", "Wyoming", "Utah" , "Oklahoma", "New Mexico"
#"Arizona" , "Alaska" , "Hawaii" ]

#num = random.randint(0 , 13)
#ranres = (states[num])
##print (ranres)

notice = input("Enter your names seperated by commas\n")
names = notice.split(", ")

#lis = len(names)
#ran = random.randint(0, lis - 1)
payee = random.choice(names)
#aha = names[ran]
print (f"{payee} is going  pay for the meal today!")
