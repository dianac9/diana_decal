# 1. Debugging : I will add a list of the de-bugging examples as they coem up below:

# In 2.2: 1 bug: forgot to include a ":" after the new defined function, so I added it and it resolved itself.
# In 2.3: 1 bug: Tried to get it to print the other list sliced as a function, said it was not subscriptable, so I went back and changed the new list into a variable.
# In 3.1: 1 bug: had a lot of difficulties with actually getting the results to rpint, finally found a way through looking at stackoverflow

# 2. Practicing Slicing and Striding

#2.1 Making a List Variable
# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually. 

list_a = [0]
n = 0
while n < 20:
    n += 1
    list_a.insert(len(list_a), n)
print(list_a)
# No bugs

#2.2 Working with List Elements
# Write a function that will take in your list from Part 2.1 and square each element
# in the list. Assign the result to a new variable


def list_squared(list_a):
    return [n ** 2 for n in list_a]

squared_list = list_squared(list_a)
print(squared_list)


# 1 bug: forgot to include a ":" after the new defined function, so I added it and it resolved itself.


#2.3 Slicing
# Write a function that takes in your new list from Part 2.2 and returns the first
# 15 elements of the list using slicing.

def list_sliced(squared_list):
    return squared_list[0:15:1] #change 15 to 16 if you want 15 squared in the list as well.
print(list_sliced(squared_list))

# 1 bug: Tried to get it to print the other list sliced as a function, said it was not subscriptable, so I went back and changed the new list into a variable.

#2.4 Striding
# Write a function that takes in your list from Part 2.2 and returns every 5th
# element from the list using striding.

def list_stride(list_sliced):
    return squared_list[0:21:5]
print(list_stride(squared_list))

#2.5 Slicing and Striding
# Write a function that takes your list from Part 2.2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.
def list_slice_and_stride(squared_list):
    last_three = squared_list[-3:]
    last_three_reversed = last_three[::-1]
    return last_three_reversed[::3]

print(list_slice_and_stride(squared_list))


# 3. 2D Lists

#3.1 Creating a 5x5 2D List
# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.

def create_grid_5x5():
    grid = []
    number = 1

    for row in range(5):
        row_list = []
        for col in range(5):
            row_list.append(number)
            number += 1
        grid.append(row_list)
    return grid
grid = create_grid_5x5()
for row in grid:
    print(row)
        
#1 bug: had a lot of difficulties with actually getting the results to rpint, finally found a way through looking at stackoverflow


#3.2 Replacing 2D List with Multiples of 3
# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”
def replace_mult_3(grid):
    for row in range(5):
        for col in range(5):
            if grid[row][col] % 3 == 0:
                grid[row][col] = "?"
    return grid

grid = create_grid_5x5()

modified_grid = replace_mult_3(grid)

for row in modified_grid:
    print(row)

# no bugs

#3.3 Summing None-'?' Elements
# Assign the result of your function from Part 3.2 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.

def sum_remaining_variables(grid):
    total = 0

    for row in grid:
        for number in row:
            if number != "?":
                total += number
    return total

grid = create_grid_5x5()
modified_grid = replace_mult_3(grid)

result = sum_remaining_variables(modified_grid)
print("Sum of non-? elements:", result)
