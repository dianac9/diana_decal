# HW 3 - Data types, Functions, Conditionals, and Loops

#1. Oski Stole Your Power
# Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
# a different way (by writing a function) that can compute x raised to the power
# of y.

def replacement_pow(x, p):
    result = 1
    for _ in range(p):
        result *= x
    return result

print ("1. The output for problem 1 is", replacement_pow(3, 0))
    



#2. What Should I Wear?
# You are trying to decide what to wear to the Python DeCal lecture, but you
# are only concerned about the day’s lowest and highest temperatures. Write a
# function that takes in a list as input and returns a tuple with the min and max
# as two values.

def hi_lo_temps(possible_temperatures):
    lowest = min(possible_temperatures)
    highest = max(possible_temperatures)
    return (lowest, highest)
possible_temperatures = [66, 32, 44, 55, 7]
print ("2. The highs and lows for this week are", hi_lo_temps(possible_temperatures))
    
    

#3. Check if its the Weekend
# All your classes have assigned problem sets due next week, and you want to
# check if it’s the weekend so you have time to work on them. Write a function
# that takes a day of the week (represented as an integer, where 1 = Monday,
# 2 = Tuesday, etc) and returns True if its a weekend and False if otherwise.

def weeknd(x):
    if 6 <= x <= 7:
        True
        return "it's the weekend...cool."
    if 1 <= x <= 5:
        False
        return "NO."
    else:
        return "Enter a number 1-7 to figure out which day it is."
print(weeknd(6))


#4. Fuel Efficiency Calculator
# The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
# CA) and they want to pick the best car. Write a function that takes the distance
# traveled (in miles) and the amount of fuel consumed (in gallons) as input and
# returns the fuel efficiency.

def fuelEff(distance, fuel):
    return (distance / fuel)
distance = 15
fuel = 2
print ("The fuel efficiency for 4 is", fuelEff(distance, fuel))


#5. Secret Code 
# Write a function that takes an integer as input and moves its last digit to the
# front of the number. You may NOT convert the input to a string. Hint: Try
# modulus (%) and floor division. (\\) to solve this problem

def mysterious_and_indie(x):
    print (x % 10, x // 10, sep="")
print (mysterious_and_indie(123456789))

#6. Min & Max but with Loops!
# Oh no! Oski hacked you computer again... now you have lost the ability to use
# min() and max().



#6.1 For Loops
# Write two functions to manually find the minimum and maximum values in a
# list of numbers with for loops.

#6.2 While Loops
# Write two functions to manually find the minimum and maximum values in a
# list of numbers with while loops.

#7. Counting Vowels
# Write a function that takes a string as an input and returns the number of vowels
# in the string and the number of consonants in the string as tuple. Don’t forget
# about capital letters! Hint: You can use .isalpha() to check if a character is 
# a letter.

def mysteriousFunction(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)

text = "Cool beans, man."
print("The number of vowels and consonants for 7 is", mysteriousFunction(text))

#8. Calculate Digital Root
# Write a function that takes an integer as an input and returns the sum of its
# digits.

#num = 2468
def digital_root(num):
    return sum(int(digit) for digit in str(num))
num = 2468
print (digital_root(num))
# str(num)
# [int(digit) for digit in str(num)]
# [2, 4, 6, 8]
