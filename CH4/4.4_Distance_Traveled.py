# Write a program that prompts the user to enter the speed of vehicle
# and the distance to be traveled. Then, it calculates and displays the time taken to travel that distance

# variables to hold speed and hours travled
speed = float(input('What is the speed of the vehicle in MPH: '))
hour = int(input('How many hours has the vehicle travled: '))

# variable to hold distance
distance = 0

print('Hour\t\t', 'Distance Travled')
print('-' * 30)
# loop to calculate distance travelled for each hour
for i in range(1, hour + 1):
    print(format(i, '1.0f'), '\t\t', format(i * speed, '6.1f'))
    distance += i * speed