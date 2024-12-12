# Write a program that asks the user to enter a number of seconds 

number_of_seconds = int(input("Please Enter The number of seconds : "))

# Let save the flowing values in variable first 
one_minute = 60
an_hour = 3600 
seconds_in_day = 86400 

# Calculate All the Results
number_of_minutes = number_of_seconds // one_minute
number_of_hours = number_of_seconds // an_hour
number_of_days = number_of_seconds // seconds_in_day

# check All the conditions and display the Result
if number_of_seconds >= 0  and number_of_seconds  < one_minute:
    print(f"is only {number_of_seconds} seconds")
elif number_of_seconds >= one_minute  and number_of_seconds  < an_hour:
    print("there is : " + str(number_of_minutes) + " minutes in " + \
          str(number_of_seconds) + " seconds ")
elif number_of_seconds >= an_hour and number_of_seconds  < seconds_in_day:
    print("there is : " + str(number_of_hours) + " hours in " + \
          str(number_of_seconds) + " seconds ")
elif number_of_seconds >= seconds_in_day :
    print("there is : " + str(number_of_days) + " days in " + \
          str(number_of_seconds) + " seconds ")