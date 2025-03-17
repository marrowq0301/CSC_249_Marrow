'''
Date:  3/16/2025
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

# Binary Search Recursively.

def linear_search(numbers, key):
    for i in range(len(numbers)):
       if (numbers[i] == key):
           return i
    return -1  # not found

# Main program to test the linear_search() method   
numbers = [3, 5, 6, 15, 18, 24, 43, 69, 74, 81]
     
key = int(input('Enter a number: '))
key_index = linear_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found. It is not a binary number on record.' % key)
else:
    print('Found %d at index %d.  It is a binary number on record.' % (key, key_index))
