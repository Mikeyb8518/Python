# Write a program that uses is_prime function that will display prime numbers from 1-100

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Define a function to display prime numbers from 1-100
def prime_list(limit):
    primes = []
    for num in range(1, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# set limit to 100
limit = 100
# call the function and print the result
print(prime_list(limit))