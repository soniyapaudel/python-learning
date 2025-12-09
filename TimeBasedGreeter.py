# Good Morning Sir 

""" Create a Python Program capable of gretting you with Good morning.
    Good Afternonn and Good Evening. Your Program should use time module to get the current hour.
    Here is sample program and documentation link for you.
  """


import time 
current_time = time.strftime('%H:%M:%S ')
print("Current time is: ", current_time)

hour = int(time.strftime('%H'))
print(hour)

if( 5 <= hour <= 9):
    print("Good Morning")
elif(10 <= hour <= 17):
    print("Good Afternoon")
elif( 18 <= hour <= 20):
    print("Good Evening")
else:
    print("Good Night")