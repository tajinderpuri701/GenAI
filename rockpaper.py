import random
flag=True
choices = ["rock", "paper", "scissor"]
computer_score=0
user_score=0
no_of_draws=0
while flag:
    computer_choice = random.choice(choices)
    computer_choice1 = computer_choice[0]
    computer_choice1=computer_choice1.lower()
    user_choice = input("enter (R)ock or (P)aper or (S)cissors or enter (Q) to quit :").lower()
    if user_choice=="q":
        print(f"you won {user_score} times")
        print(f"computer won {computer_score} times")
        print(f"there were {no_of_draws}")
        with open('score.txt','W') as score_file:
            score_file.write(f"you won {user_score} times\n")
            score_file.write(f"computer won {computer_score} times\n")
            score_file.write(f"there were {no_of_draws} draw")
        break
    if user_choice not  in ["r", "p", "s"]:
        print("enter only from options given!")
        continue
    else:
        if computer_choice1=="r" and user_choice=="p":
            print(f"the computer chose {computer_choice}")
            print("you won")
            user_score+=1

        elif computer_choice1=="r" and user_choice=="s":

            print(f"the computer_chose {computer_choice}")
            print("you lost")   
            computer_score +=1
        elif computer_choice1=="s" and user_choice=="p":
            print(f"the computer chose {computer_choice}")
            print("you lost")
            computer_score +=1
        elif computer_choice1=="s" and user_choice=="r":
            print(f"the computer chose {computer_choice}")
            print("you won")
            user_score +=1
        elif computer_choice1=="p" and user_choice=="r":
            print(f"the computer chose {computer_choice}")
            print("you won")
            user_score +=1
        elif computer_choice1==user_choice:
            print("draw")
            no_of_draws+=1
