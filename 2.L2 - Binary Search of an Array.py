'''
Date:  2/17/2025
Author/Editor:  Quentin Marrow
'''

#2.L2 - Instructions

'''
So, again, get your code editor ready, enter the code for Binary search in Zybooks 2.3, and run the program.
Once you've confirmed it works, replace the values that are provided with your own.
For this assignment, you can use a list/array of int, double, or string. 
'''

# I chose to go with strings for this assignment.

def binary_search(names, key):
    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts with entire range.
    low = 0
    high = len(names) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        if (names[mid] < key):
            low = mid + 1
      
        elif (names[mid] > key):
            high = mid - 1
      
        else:
            return mid   
   
    return -1 # not found


# Main program to test the binary_search() function   
names = ["Anna", "Bill", "Chris", "Donald", "Eric", "Frank", "Gary", "Harold", "Inez", "Jack", "Kevin"]
print('Names:', names)
     
key = input('Enter a name - capitalize first letter: ')
key_index = binary_search(names, key)
     
if (key_index == -1):
    print(f' "{key}" was not found.')
else:
    print(f'Found "{key}" at index {key_index}')