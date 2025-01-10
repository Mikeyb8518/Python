# Write a program that will take the user input and determine if it is a prime number or not.
# A prime number is a number that is greater than 1 and has no positive divisors other
# than 1 and itself.

# write a function to get user input
def get_user_input():
    return int(input("Please enter a number: "))

# write a function to check if a number is prime
def is_prime(x):
    if x <= 1:
        return False
    else:
        i = 2
        while x > i:
            if x % i == 0:
                return False
            else:
                i = i + 1
        else:
            return True

def print_value(boolean):
    print(boolean)

def main():
    x = get_user_input()
    boolean = is_prime(x)
    print_value(boolean)

main()