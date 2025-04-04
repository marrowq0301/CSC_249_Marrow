'''
Date:  4/3/2025
Author/Editor:  Quentin Marrow
'''

#4.L1 - Instructions

'''
For this assignment you'll want to look way back to sections 2.2 and 2.3 of 
your Zybooks for a reference implementation.

Implement the "Linear Search" program as described in section 2 of Zybooks.

'''



def linear_search(numbers, key):
    for i in range(len(numbers)):
        if (numbers[i] == key):
            return i
    return -1  # not found

# Main program to test the linear_search() method   
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = linear_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))