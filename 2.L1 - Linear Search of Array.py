'''
Date:  2/17/2025
Author/Editor:  Quentin Marrow
'''

# 2.L1 - Instructions

'''
Instructions:
I would like you to modify the code, so that instead of the provided numbers, you use either:
- a list of floating point numbers, or
- a list of strings.
'''

# I chose to go with floating point numbers.

def linear_search(flt_pt_numbers, key):
    for i in range(len(flt_pt_numbers)):
        if (flt_pt_numbers[i] == key):
            return i
    return -1  # not found

# Main program to test the linear_search() method   
flt_pt_numbers = [1.7, 4.5, 9.2, 10.5, 14.9, 31.8, 40.2, 65.1]
print('NUMBERS:', flt_pt_numbers)
     
key = float(input('Enter a floating point value: '))
key_index = linear_search(flt_pt_numbers, key)
     
if (key_index == -1):
    print('%.1f was not found.' % key)
else:
    print('Found %.1f at index %d.' % (key, key_index))