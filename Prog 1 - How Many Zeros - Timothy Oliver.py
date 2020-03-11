##############################################
# Name: Timothy Oliver
# Date: 11 December 2019
# Description: finds the number of zeros in all integers from one to the number
# given by the user and returns the time taken to execute the function
##############################################

from time import time   # imports time for use of time() in finding function runtime

# function in which the numbers from
# 1 to endnum are iterated for use in the zero count
def findTotalZeroes(n):
    global start_time
    start_time = time()
    for i in range (1, n+1):
        findZeroes(i)
    global end_time
    end_time = time()
    return numOfZeroes
    

# finds the number of zeros in the parameter's digits
def findZeroes(num):
    while (num > 0):
        if ((num % 10) == 0):
            global numOfZeroes
            numOfZeroes += 1
        num /= 10


# MAIN
numOfZeroes = 0             # initialize these three variables in main to make output one line while allowing their manipulation in functions
start_time = 0
end_time = 0
endnum = input("What number do you want to count zeros to? ")
print "The number of zeros written from 1 to {} is {}.\nThis took {} seconds.".format(endnum, findTotalZeroes(endnum), (end_time - start_time))

