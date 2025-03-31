'''
Date:  3/30/2025
Author/Editor:  Quentin Marrow
'''

#4.T1 - Instructions

'''
Classic algorithms that are often compared with iterative vs. recursive implementations include:
Here is the general algorithm we will implement. (Use your language of choice.) In the video I will give a sample 
explanation, which you may follow, or you can implement the code yourself.
start with array of ints and an int current_max (what is a good initialization value for current_max? (0, V[0], etc.) )
given vector iterate through,

-compare each n with current_max
-if n > current_max
-----current_max = n
-when done, current_max is global max

'''

# Local Maximum

def global_max(V):
    # Checking to ensure array values are present.
    if not V:
        raise ValueError("Please check array for values.")
    
    current_max = V[0]  
    
    for n in V:
        if n > current_max:
            current_max = n
    
    return current_max

#Array and final output
peak = [1, 4, 7, 5, 3, 4]
max_value = global_max(peak)
print(f"The maximum value is: {max_value}")