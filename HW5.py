# HW 5

# 1. HW 1/ HW 2 Review: The Terminal + Command Line + Git

# 1.1 You have been plopped into this directory system. What command will tell you what your working directory is?

# A: The pwd, or print working directory command, will tell you what working directory you're in.

# 1.2 The command tells you ∼/python decal/judy decal. What command will list all the files in your current working directory?

# A: The ls command will list all of the files in your current working directory.

# 1.3 Brianna just sent out an announcement that there was a typo on homework.py. So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?

# A: 1. cd brianna_repo 2. git pull origin main(or master, depending)

# 1.4 How would you move this new homework.py to your personal repository homework directory?

# A: 1. cp homework.py diana_decal  2. cd diana_decal 3. git add homework.py 4. git commit -m "Updated homework.py without typo" 5. git push origin master(or main)

# 1.5 You want to see the contents of the homework.py in your terminal from your personal repository. What command(s) will let you do this?

# A: 1. cd diana_decal 2. cat/nano homework.py

# 1.6 You want to edit the contents of the homework.py in your terminal from your personal repository. What command will let you do this?

# A: 1. cd diana_decal 2. nano homework.py

# 1.7 You have finished the homework. What commands will allow you to save the changes and push from your local repository to your remote repository?

# A: 1. cd diana_decal 2. git status 3. git add homework.py 4. git commit -m "Completed homework and updated homework.py" 5. git push origin master(or main)

# 1.8 Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did ”Judy” do wrong?)
# ! [rejected] main -> main (fetch first)
# error: failed to push some refs to ’https://github.com /judy/judy_decal.git’
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., ’git pull ...’) before pushing again.
# hint: See the ’Note about fast-forwards’ in ’git push --help’ for details.

# A: This error occurs because the remote repository contains new changes that are not present in the local repository. This may be because updates were pushed into the main branch, making the local branch out of sync.
# A: 1. git fetch origin 2. git merge origin/main(or master) 3. git push origin main(or master)

# 1.9 What absolute path will allow you to move to Recents/?

# A:  cd ~/System/Library/Recents/

# 2. HW 3 Review: Data Types + Functions + Conditionals + Loops

# 2.1 Data Types:
# Write a function that takes any input and returns a string indicating its data type.

def get_data_type(value):
    return f"The data type of the input is: {type(value).__name__}"

print(get_data_type(43))

# 2.2 Conditionals:
# Write a function that takes an integer as input and returns ’Even’ if the integer is even, and ’Odd’ otherwise.

def evenOrodd(x):
    if x % 2 == 0:
        return "This number is even."
    else:
        return "This number is odd."
print(evenOrodd(7))

# 2.3 Loops:
# Write a function that takes a list of integers and returns their sum using a loop (do NOT use the built-in sum() function).

def sumLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print (sumLoop([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 3. HW 4 Review: Lists

# 4.1: Lists
# Write a function that takes a list and returns a new list with each element duplicated.

def dupe_list(L):
    dupe_list = []
    for item in L:
        dupe_list.append(item)
        dupe_list.append(item)
    return dupe_list
print (dupe_list([9, 5, 1]))

# 4.2: Debugging
# There’s an error in the following function that’s supposed to return the square of a number. Find and correct it:
# Original:
# def square(num)
#    return num * num

# Fixed:
def square(num):
    return num * num
print(square(5)) #To ensure it works as it should, it does.

# 5. HW2 Review: Git
# Please take a screenshot of you adding, committing and pushing this home-work from your local to your remote repository. Include this screenshot in your Gradescope submission!
#Screenshot will be included.
