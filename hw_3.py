# Name: Boxin Zhao
# hw3.py

import math
import random

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
    if (not isinstance(m, int)) or (not isinstance(n, int)):
        return "Error: Inputs are not integers!", (m, n)
    elif n == 0:
        return "Error: divisor should not be zero!", n
    else:
        if (m % n) == 0:
            return True
        else:
        
            return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function
print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # What should this return? Should cause an error
print(is_divisible(3, 1.1))  # Should cause an error
print(is_divisible(9, -3))  # Should return true
# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(x, y):
    return not (x == y)

# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(3.4, 4.2))  # This should return True
print(not_equal(4.3, 4.3))  # This should return False
print(not_equal(1 + 2j, 1 + 3j))  # This should return True
print(not_equal(1 + 2j, 1+ 2j))  # This should return False

# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a, b, c):
    return a * b + c

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test = multadd(math.cos(math.pi / 4), 1/2, math.sin(math.pi / 4)) 
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(2, math.log(12, 7), math.ceil(276 / 19))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    n = random.randint(0, 100)
    print("The integer we generate is: %d" % n)
    return (n % 3) == 0

# Test Cases
##### YOUR CODE HERE #####
print(rand_divis_3())

