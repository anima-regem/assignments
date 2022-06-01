import random

choice_list = ['stone', 'paper', 'scissors']
comp_score, user_score = 0,0
for i in range(4):
    user_choice = input('Enter your choice [stone/paper/scissors] : ')
    comp_choice = random.choice(choice_list)
    if(comp_choice!=user_choice):
        if(((user_choice == 'paper') and (comp_choice=='scissors')) or ((user_choice == 'stone') and (comp_choice=='paper')) or ((user_choice == 'scissors') and (comp_choice=='stone'))):
            comp_score+=1
        else:
            user_score+=1
if(user_score>comp_score):
    print("You won!!!")
elif(user_choice<comp_choice):
    print("Computer won!!!")
else:
    print("Tie!!!")