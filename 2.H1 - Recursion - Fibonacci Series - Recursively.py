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

# Fibonacci Series Recursively.


def fibonacci_number(term_index):
    if term_index == 0:
        return 0
    elif term_index == 1:
        return 1
    else:
        return fibonacci_number(term_index - 1) + fibonacci_number(term_index - 2)

if __name__ == "__main__":
    user_input = input("Enter the number of Fibonacci sequence numbers to display: ")
    try:
        count = int(user_input)
        if count < 1:
            print("Please enter a positive integer.")
        else:
            for i in range(count):
                print(f"Fibonacci({i}) = {fibonacci_number(i)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
