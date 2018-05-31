"""This is a calendar program. Features include: viewing the calendar, adding events, updating events, and deleting events. It will also print a welcome message to the user, prompt the user to view, add, update, or delete events on the calendar. The program will not terminate unless the user decides to exit."""

# Import neccessary functions
from time import sleep, strftime 

# initialize variables
USER_NAME = "Kristin" 
calendar = {}

# This function welcomes the user, informs them of today's date and time, and asks them what they would like to do. 
def welcome():
  print("Welcome back, " + USER_NAME + ".")
  print("Calendar opening...")
  sleep(1)
  print("Today is " + strftime("%A, %B %d, %Y") + ".")
  print("The time is now " + strftime("%I:%M:%S") + ".")
  sleep (1)
  print("What would you like to do? ")

# This function runs the relevant commands depending on the users input. 
# The while loop ensures that the user would like to keep interacting with the calendar program. 
# The if/elif/else statements within the while loop execute the A/U/V/D actions.
def start_calendar(): 
  welcome()
  start = True 
  while start == True: 
    user_choice = input("Please enter A to add an event, U to update an event, V to view an event, D to delete an event, and X to exit. ")
    user_choice = user_choice.upper()
    if user_choice == "V": 
      if len(calendar.keys()) < 1: 
        print("Your calendar is empty.")
      else: 
        print(calendar)
    elif user_choice == "U": 
      date = input("What is the date of the event? ")
      update = input("What is your update? ")
      calendar[date] = update
      print("Event successfully updated!")
      print(calendar) 
    elif user_choice == "A": 
      event = input("What is the event? ")
      date = input("What is the date of the event? Please use the format MM/DD/YYYY. ")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")): 
        print("Invalid date. Please re-enter. ")
        try_again = input("Would you like to try again? Enter Y for yes and N for no. ")
        try_again = try_again.upper()
        if try_again == "Y": 
          continue
        else: 
          start = False 
      else: 
        calendar[date] = event 
        print("Event successfully added!")
        print(calendar) 
    elif user_choice == "D": 
      if len(calendar.keys()) < 1: 
        print("Your calendar is empty.") 
      else: 
        event = input("What is the event?")
        for date in calendar.keys(): 
          if event == calendar[date]: 
            del calendar[date]
            print("Event successfully deleted!")
            print(calendar) 
          else: 
            print("No such event found.")
    elif user_choice == "X": 
      start = False 
    else:
      print("Incorrect value entered.")
      start = False 

# This command runs the calendar program    
start_calendar()
