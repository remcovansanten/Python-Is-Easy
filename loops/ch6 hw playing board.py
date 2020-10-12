"""
Homework Assignment #6: Advanced Loops
Author: Remco van Santen

Details:
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified. After drawing the board, your function should return True.
"""
def draw_playingboard(columns, rows):
    print('*'*15)
    print('First Solution')
    print('*'*15)
    print('')
    if columns == 1:
        print('Columns must be greater than 1')
        return False
    else:
       for r in range(rows*2):  # Needs to be doubled because need to print to lines for each row
           if r%2 == 0:  # Determine odd and even rows
               # even lines
               for c in range(columns):
                   if c < columns-1:             # Check if it is the last column
                       print('  |  ', end = '')  # Print and stay on same line
                   else:
                       print(' ')              # Print and move to next line
           else:
               # Odd lines
               if r != 2*rows-1:  # Don't print the last line
                print('-----' * (columns-1))
       return True


# Alternative solution
# Prints a playing board with surrounding borders
def draw_playingboard_alt(columns, rows):
    print('*'*20)
    print('Alternative Solution')
    print('*'*20)

    print('---' * columns)
    for r in range(rows):
        print('|  ' * (columns + 1))
        print('---' * columns)
    return True


print(draw_playingboard(8 , 3) )
#print(draw_playingboard_alt(12,3) )
