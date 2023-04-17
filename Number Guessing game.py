import random

def prime_check(p):
    if p <=1:
        return False
    if p <= 3:
        return True
    if p %2 == 0 or p %3 == 0:
        return False
    i = 5
    while i<=p:
        if p %i ==0 or p %(i+2) ==0:
            return False
        i +=6
        return True
    
tries = 0
hints = 0

n = random.randrange(1,501)
print("Welcome To 'Guess The Number'.")
print(" ")
print("The Game is Very simple, Computer will choose a number between 1-500 and you have to guess that number within 10 tries.'")
print(" ")
print("If You are having a hard time guessing You can Give up Or ask For a hint using 'give up' or 'hint' Commands.")
print(" ")
print("Note: There Is a 1 Guess Cooldown on Hints")
print(" ")

guess = (input("Enter any number: "))
while guess!=n:
     if guess == "give up":
        print("Youe Gave up the number was", n)
        break
     if guess == "f":
        print("")
        print(n)
        print("")
        guess = (input("Try Again ---> "))
     if guess == "hint":
        h_type= random.randint(1,2)
        if h_type==1:
           if n %2 == 0:
              print(" ")
              print("The Number Is Even")
              print(" ")
              guess = (input("Try Again ---> "))
              hints+=1
           else:
              print(" ")
              print("The Number is Odd")
              print(" ")
              guess = (input("Try Again ---> "))
              hints+=1 


        if h_type==2:
           if prime_check(n):
              print(" ")
              print("The Number is a Prime Number")
              print(" ")
              guess = (input("Try Again ---> "))
              hints+=1 
           else:
             print(" ")
             print("The Number is Not a Prime Number")
             print(" ")
             guess =  (input("Try Again ---> "))
             hints+=1


     if guess.isdigit():
           tries += 1
           left = 10-(tries)
           guess=int(guess)
           if guess < n:
             print(" ")
             print("Guess was Too low")
             print(left, (" Tries Left."))
             print(" ")
             guess =(input("Try Again ---> "))
           elif guess > n:
              print(" ")
              print("Guess was Too high!")
              print(left, (" Tries Left."))
              print(" ")
              guess = (input("Try Again ---> "))
           elif guess==n:
              print(" ")
              print("You guessed Correctly in", tries,("Tries and used"), hints,("Hints"))
              break
           if tries == 10:
             print(" ")
             print("10 Tries completed You lost the Game.")
             break
     else:
        print(" ")
        guess=input("Invalid Input Try Again ---> ")