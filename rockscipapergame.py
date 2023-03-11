import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock , scissors , paper]

computer_choose = random.randint(0, 2)
com_images= (game_images[computer_choose])


#User Choice logic

user_choose = int(input("Type '0' for rock , '1' for sciccors and '2' for paper\n"))
u_image= (game_images[user_choose])
if user_choose > 2 or user_choose < 0:
  print("You have entered an invalid input.")
else:
    print (f"User choose {u_image}")

    print (f"Computer choose {com_images}")
        #The Game Logic

    if user_choose == 0 and computer_choose == 2 :
        print ("You Win!")
    elif user_choose > computer_choose:
        print ("You Win!")
    elif user_choose == computer_choose :
            print("It's a draw!")
    else:
        print("You Lost")
        
