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

def normal(num, mean, std_dev):
    """
    Returns: 
        value of a random varible given it follows a Normal Distribution
    Args: 
        num:     random variable
        mean:    mean of the gaussian disttribution
        std_dev: standard deviation of the gaussian distribution
    """
    constant = 1 / (std_dev * np.sqrt(2*np.pi))
    exponent = (num - mean)**2 / (2 * (std_dev**2))
    return constant * np.exp(-exponent) 

##########################################################################################################
# Helper Functions
##########################################################################################################

def factorial(num):
    assert isinstance(num, int), f"Number must be an integer, got {type(num)}"
    assert num >= 0, f"Number must be >= 0, got {num}"

    if num == 0:
        return 1

    return num * factorial(num - 1)
    
def combination(num, k):
    return int(factorial(num) / (factorial(k) * factorial(num - k)))

def permutation(num, k):
    return int(factorial(num) / factorial(num - k))

if __name__ == "__main__":
    # print(factorial(-5))
    # print(combination(2, 1))
    
    # dice roll example
    start = 1
    n = 10
    p = 0.5
    binomial_list = []
    normal_list = []
    for k in range(n+1):
        binomial_list.append(binomial(n, k, 0.5))
        normal_list.append(normal(k, mean=n*p, std_dev=np.sqrt(n*p*(1-p))))
    plt.plot(binomial_list, "b-", label="Binomial", linewidth=3)
    plt.plot(normal_list, "r", label="Normal")
    plt.legend()
    plt.xlim(0, n)
    plt.show()




