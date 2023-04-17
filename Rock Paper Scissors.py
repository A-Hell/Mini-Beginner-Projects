import random

options = ["rock", "paper", "scissors"]

play_again = True

u_wins=0
c_wins=0

while play_again == True:
  
  N= random.randint(0,2)

  uc = input("Rock Paper Scissors... Shoot : ").lower()

  while True:

    if uc== "q":
        play_again = False
        break
        
    
    if uc not in options:
     uc= input("Invalid Input Try Again: ").lower()

    c= options[N]

    print(c)
    if uc == c:
      print("")
      print("Its A Tie.")
      print(" ")
      break

         
    elif uc == "rock" and c == "scissors":
              print(" ")
              print ("Computer Picked ",c)
              print(" ")
              print("Congrats! You Won.")
              print(" ")
              u_wins += 1
              break
    

    elif uc == "paper" and c == "rock":
        print(" ")
        print ("Computer Picked ",c)
        print(" ")
        print("Congrats! You Won.")
        print(" ")
        u_wins += 1
        break

    elif uc == "scissors" and c == "paper":
        print(" ")
        print ("Computer Picked ",c)
        print(" ")
        print("Congrats! You Won.")
        print(" ")
        u_wins += 1
        break
        
    else:
        print("")
        print ("Computer Picked ",c)
        print(" ")
        print("Oops! You Lost.")
        print(" ")
        c_wins+=1
        break





print(" ")
print("You Won ", u_wins," Times.")
print("Computer Won", c_wins, "Times.")
print(" ")
print("GoodBye")
