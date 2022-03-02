
# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0
#     Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    for i in range(num,0,-1):
        print(i)
print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(a, b):
    print(a)
    return 2
print(print_and_return(1,2))

# First Plus Length - Create a function that accepts a list and 
# returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(arr):
    sum=arr[0]+len(arr)
    return sum
print(first_plus_length([1,2,3,4,5]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(a,repeat):
    print(str(a) * repeat)
print(length_and_value(4,7))
print(length_and_value(6,2))