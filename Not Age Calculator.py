from datetime import date

name = input("Enter Your name to begin: ").title()
print(f"\nHello {name}, This app will tell you your age down to the last day.")
print("\nYou Just Put in Your BirthDate and leave the rest to Me.")
print("")

valid_data = True

date_range = range(1,33)
month_range = range(1,13)
month_in_minus = range(-12, 0)
day_in_minus = range(-32, 0)


today = str(date.today()).split('-')

today_day = int(today[2])
today_month = int(today[1])
today_year = int(today[0])


while True :
    birthday_Date = int(input("Day = "))
    birthday_Month = int(input("Month = "))
    birthday_Year = int(input("Year = "))

    # Data validation

    if birthday_Date in date_range and birthday_Month in month_range and (today_year >= birthday_Year > 0):
       print(".\n..\n...\n....\n.....")
    if birthday_Month % 2 == 0 and 0 < birthday_Date < 31:pass
    elif birthday_Month % 2 == 1 and 0 <birthday_Date <32:pass
    elif birthday_Month == 2 and 0 < birthday_Date <30:pass
    else:
       print("Not a Valid response try again")
       valid_data = False

    # Calculator
    if valid_data == True:
        age_year = today_year - birthday_Year
        age_month = today_month - birthday_Month
        age_day = today_day - birthday_Date

        if age_day in day_in_minus:
            if birthday_Month == 2:
               if birthday_Year % 4 == 0:
                 age_day = 30 + age_day
               else: age_day = 29 + age_day
            elif age_month % 2 == 1:
             age_day = 31 + age_day
            else:
              age_day = 30 + age_day
              age_month -= 1

        if age_month in month_in_minus:
            age_year -=1
            age_month = 12 + age_month

        print("\nCalculations Completed")
        print(f'\n{name}, you currently are {age_year} Years, {age_month} Months and {age_day} Days Old')

        exit = input('\nEnter anything to restart or press enter to exit: ')
        if exit == "":
          break
        else : pass