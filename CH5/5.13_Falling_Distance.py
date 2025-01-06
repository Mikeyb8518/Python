# Write a function called falling distance, that accepts an objects falling time in seconds
# as an argument. The function should return the distance in meters., that the object has fallen.

# Function to calculate falling distance
def falling_distance(i):
    # formula to calculate distance = 0.5 * g * t^2
    d = (1 /2) * 9.81 * (i**2)
    # Print the distance
    print(format(d, '6.2f'), ' meters')
    # Return the function
    return d

# for loop to calculate the distance for each second from 1 to 10
for i in range(1, 11):
    falling_distance(i)  # Call the function with the loop variable i