import numpy as np
import matplotlib.pyplot as plt

##########################################################################################################
# Probability Distributions
##########################################################################################################

def binomial(num, k, p):
    """
    Returns: 
        value of a random varible taking a value 'k' given it follows a Binomial Distribution
    Args: 
        num: number of independent bernoulli distributions
        k:   random variable being k (success)
        p:   probability of success
        q:   probability of failure = 1 - p
    """
    return combination(num, k) * (p**k) * ((1 - p)**(num - k))

##########################################################################################################
# Helper Functions
##########################################################################################################

def factorial(num):
    assert isinstance(num, int), print(f"Number {num} must be an integer, but received type {type(num)}.")
    assert (num >= 0), print(f"Number must be greater than or equal to 0, but received {num}.")
    return int(num) if ((num - 1) == 0) else num * factorial(num - 1)
    
def combination(num, k):
    return int(factorial(num) / (factorial(k) * factorial(num - k)))

def permutation(num, k):
    return int(factorial(num) / factorial(num - k))

if __name__ == "__main__":
    # print(factorial(-5))
    print(combination(2, 1))
