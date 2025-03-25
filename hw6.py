

#HW 6 - NumPy Arrays


# 1: Prime Clusters
# You have obtained a dataset of star temperatures from different stellar clusters.
# For your research, you are interested only in clusters where at least one star’s
# temperature is a prime number. Given a 2D NumPy array, write a function to
# find the rows where at least one value is a prime number. For example:
# >>> arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
# >>> containsPrimes(arr)
# array([[2, 3, 5],
# [11, 13, 17],
# [7, 10, 13]])

import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    mask = np.array_along_axis(lambda row: any(is_prime(x) for x in row), axis = 1, arr = arr)
    return arr[mask]

# 2: Let's Play Checkers!
# You’ve decided to take a break from your cutting-edge research and play checkers
# with your friend. Unfortunately, there is no checkerboard in sight! Therefore
# you must create one yourself.

# 2.1: Start by writing a function that creates a 8x8 square matrix with only zeros.
# 2.2: For only the odd rows, make an alternating pattern of ones and zeroes.
# 2.3: Finish the checkerboard with the even rows.

def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board

# 2.4: Re-write your function such that the checkerboard begins with a 0 instead.

def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, 1::2] = 1
    board[1::2, ::2] = 1
    return board

# 3: The Expanding Universe
# You have now become fascinated with how dark energy is making galaxies
# accelerate away from us. Write a function that takes in a string and a number,
# and returns the string with the specified number of spaces inserted between each
# letter, simulating the expansion of space!

def expansion(arr, spaces):
    expand = lambda s: (' ' * spaces).join(list(s))
    vectorized_expand = np.vectorize(expand)
    return vectorized_expand(arr)

# 4: Second-Dimmest Star
# While analyzing a dataset of star luminosities, you need to identify the second-
# dimmest star in each cluster. Write a function that takes a 2D NumPy array
# and returns an array containing only the second-smallest value in each column.

def secondDimmest(arr):
    return np.sort(arr, axis=0)[1]
