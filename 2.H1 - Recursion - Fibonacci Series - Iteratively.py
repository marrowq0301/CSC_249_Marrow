'''
Date:  3/6/2025
Author/Editor:  Quentin Marrow
'''

#2.H1 - Instructions

'''
Classic algorithms that are often compared with iterative vs. recursive implementations include:
-Factoral
-Fibonacci Series
-Binary search
For 2.H1, I would like you to pick any two of these, and implement them both iteratively and recursively.
'''

# Fibonacci Series Iteratively.

def linear_search(fib_numbers, key):
    for i in range(len(fib_numbers)):
       if (fib_numbers[i] == key):
           return i
    return -1  # not found

# Main program to test the linear_search() method   
fib_numbers = [0, 1, 2, 3, 5, 8, 13, 21, 24, 34, 55]
     
key = int(input('Enter a fibonacci value: '))
key_index = linear_search(fib_numbers, key)
     
if (key_index == -1):
    print('%d was not found. It is not a fibonacci number.' % key)
else:
    print('Found %d at index %d.  It is a fibonacci number.' % (key, key_index))
