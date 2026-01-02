import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from typing import Optional

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
        value of a random varible given it follows a Normal Distribution, 
        also serves as an approximation of the Binomial Distribution when n & p are neither very small nor very large
    Args: 
        num:     random variable
        mean:    mean of the gaussian disttribution
        std_dev: standard deviation of the gaussian distribution
    """
    constant = 1 / (std_dev * np.sqrt(2*np.pi))
    exponent = (num - mean)**2 / (2 * (std_dev**2))
    return constant * np.exp(-exponent) 

def poisson(num, k, p):
    """
    Returns: 
        value of a random varible given it follows a Poisson Distribution (approxmation of Binomial Distribution when 'p' is either very small or very large)
    Args: 
        num: number of independent bernoulli distributions
        k:   random variable being k (success)
        p:   probability of success
        q:   probability of failure = 1 - p
    """
    lmd = num * p
    return ((lmd**k) / factorial(k)) * np.exp(-lmd)

def geometric(num, p, case="exact"):
    """
    Returns: 
        probability of success at "exactly" n'th trial, considering all n trials are independent bernoulli distributions
    Args: 
        num: number of independent bernoulli distributions
        p:   probability of success
    Note:
        p(x >= n) = (1-p)^(n-1), case where it takes "at least" n independent bernoulli trials to get success
    """
    if case=="exact":
        return ((1 - p)**(num - 1))*p 
    elif case=="at_least":
        return (1 - p)**(num - 1)
    
##########################################################################################################
# Helper Functions
##########################################################################################################

def cdf(num, mean, std_dev):
    X = np.linspace(start=-5*std_dev, stop=5*std_dev, num=10)
    normal_dist = []
    for x in range(len(X)):
        normal_dist.append(normal(X[x], mean, std_dev))
    return quad(lambda x: normal(x, mean, std_dev), a=-np.inf, b=num)

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
    n = 100
    p = 0.01
    binomial_list, normal_list, poisson_list = [], [], []
    for k in range(n+1):
        binomial_list.append(binomial(n, k, p))
        normal_list.append(normal(k, mean=n*p, std_dev=np.sqrt(n*p*(1-p))))
        poisson_list.append(poisson(n, k, p))
    plt.plot(binomial_list, "b+", label="Binomial", linewidth=3)
    plt.plot(normal_list, "r*", label="Normal")
    plt.plot(poisson_list, "g", label="Poisson")
    plt.legend()
    plt.xlim(0, n)
    # plt.show()

    # value, error = cdf(1, 0, 1)
    # print(value)

    print(geometric(2, 1/6))





